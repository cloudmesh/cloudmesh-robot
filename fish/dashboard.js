var speedThrottle = 200;
var allowRequest = true;

var lastRobot = {}
var curRobot = {}

var $readout = $('#readout');
var $console = $('#console');

$(function(){    
    $robotSelect = $('#robotSelect');
    fish = fish['fish']
    
    // create robot radio buttons
    $.each(fish, function(i, robot){
        var $p = $('<p>');
        var $radio = $('<input type="radio" name="robots" value="' + i + '"/>');
        if(i == 0){
            $radio.attr('checked', 'checked');
            curRobot = robot;
        }
        var $label = $('<label for="' + robot.name + '">' + robot.name + '</label>');
        $p.append($radio);
        $p.append($label);
        $robotSelect.append($p);
    });
    
    $('#robotSelect input:radio').click(function(){
        lastRobot = curRobot;
        curRobot = fish[$(this).val()];
        updateConsoleLeft();
    });
    
    makeGauge();
    
    // key pressed
    $('#keys li').click(function(){        
        index = $(this).index();
        switch(index){
            case 0:
                params = 'SWIM=1'
                break;
            case 1:
                params = 'LEFT=ON';
                break;
            case 3:
                params = 'RIGHT=ON';
                break;
            case 4:
                params = 'MIDDLE=ON';
                break;
        }
        
        sendRequest(params);
    });
    
    // end
    $('#end').click(function(){
        sendRequest('END=ON');
    });
    
    $('#up').click(function(){
        sendRequest('UP=ON');
    });
    
    $('#down').click(function(){
        sendRequest('DOWN=ON');
    });
});

function makeGauge(){
    var minValue = 29;
    var maxValue = 115;
    var middle = (maxValue + minValue) / 2;

    var opts = {
        angle: 0, // The span of the gauge arc
        lineWidth: 0.44, // The line thickness
        radiusScale: 1, // Relative radius
        pointer: {
            length: 0.6, // // Relative to gauge radius
            strokeWidth: 0.035, // The thickness
            color: '#000000' // Fill color
        },
        limitMax: true,     // If false, the max value of the gauge will be updated if value surpass max
        limitMin: true,     // If true, the min value of the gauge will be fixed unless you set it manually
        colorStart: '#6FADCF',   // Colors
        colorStop: '#6FADCF',    // just experiment with them
        strokeColor: '#6FADCF',  // to see which ones work best for you
        generateGradient: true,
        highDpiSupport: true     // High resolution support
    };
    var target = document.getElementById('finGauge'); // your canvas element
    var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
    gauge.maxValue = maxValue; // set max gauge value
    gauge.setMinValue(minValue);  // Prefer setter over gauge.minValue = 0
    gauge.animationSpeed = 1; // set animation speed (32 is default value)
    gauge.set(middle); // set actual value
    
    $readout.text(middle);
    
    var clicked = false;
    var gaugeWidth = gauge.canvas.clientWidth;
    var realValue = middle;
    
    $('#finGauge').mousedown(function(){
        clicked = true;
    }).mouseup(function(){
        clicked = false;
    }).mousemove(function(evt){
        if(clicked){
            mouseX = evt.offsetX;
            value = Math.floor((mouseX / gaugeWidth) * (maxValue + minValue))
            realValue = maxValue + minValue - value;
            if(realValue > maxValue){
                realValue = maxValue;
            }
            else if(realValue < minValue){
                realValue = minValue;
            }
            gauge.set(value);
            $readout.text(realValue);
        }
    });
    
     // test angle
    $('#test').click(function(){
        sendRequest('ANGLE=' + realValue);
    });
    
    // set offset
    $('#offset').click(function(){
        sendRequest('OFFSET=' + (realValue - middle));
    });
    
    // reset back to middle
    $('#reset').click(function(){
        sendRequest('ANGLE=' + middle);
        
        setTimeout(function(){  
            sendRequest('OFFSET=0');
        }, 200);
        
        gauge.set(middle);
        $readout.text(middle);
    });
    
    
    
    
    // synchronous AJAX commands
    // attribution: http://voidcanvas.com/synchronous-ajax-with-es6-generators/
    var syncTaskPointer = null;
    var requestsQueue = [];
    var requestResolveCallbackQueue = [];
     
    function nativeAjax(url) {
        //this is your actual ajax function 
        //which will return a promise

        //after finishing the ajax call you call the .next() function of syncRunner
        //you need to put it in the suceess callback or in the .then of the promise
        console.log(url);
        $.ajax({url: url, timeout: 5000}).then(function(responseData) {
	        (requestResolveCallbackQueue.shift())(responseData);
	        syncTaskPointer.next();
        }).fail(function(response){
            syncTaskPointer = null;
            requestsQueue = [];
            requestResolveCallbackQueue = [];
            console.log('network failure');
        });
    }
     
    function* syncRunner(){
        while(requestsQueue.length > 0){
	        yield nativeAjax(requestsQueue.shift());	
        }
     
        //set the pointer to null
        syncTaskPointer = null;
        console.log("complete");
    };
     
    ajaxSync = function(url) {
        requestsQueue.push(url);
        if(!syncTaskPointer){
	        syncTaskPointer = syncRunner();
	        syncTaskPointer.next();
        }
        return new Promise(function(resolve, reject) {
	        var responseFlagFunc = function (data) {
		        resolve(data);
	        }
	        requestResolveCallbackQueue.push(responseFlagFunc);
        });
    }
    
    $('#run').click(function(){
        //clear old errors
        $('#console .error').remove();
        
        commands = $console.text().split('\n');
        
        // remove empty elements from array
        commands = commands.filter(entry => entry.trim() != '');
        
        regularCommands = ['left', 'right', 'middle', 'up', 'down'];
        valueCommands = ['swim', 'angle'];
        
        errors = [];
        
        // check for errors
        for(var c = 0; c < commands.length; c++){
            commandLine = commands[c].trim().split(' ');
            command = commandLine[0].toLowerCase();
            value = commandLine.length > 1 ? commandLine[1] : 'ON';
            var error = ''
            
            if(regularCommands.indexOf(command) == -1 && valueCommands.indexOf(command) == -1){
                error = 'Invalid command "' + command + '"';
            } else if(regularCommands.indexOf(command) != -1 && value != 'ON'){
                error = 'Command "' + command + '" does not accept a value';
            } else if(valueCommands.indexOf(command) != -1 && isNaN(value)){
                error = 'Command "' + command + '" requires integer value';
            } else if(command == 'angle' && Math.abs(middle - value) > 53){
                error = 'Angle is too high or low, must be within 53 units of middle (' + middle + ')';
            }
            
            if(error){
                errors.push('Error (line ' + (c + 1) + '): ' + error);
            }
        }
        
        if(errors.length){
            var div = null;
            
            for(var e = 0; e < errors.length; e++){
                error = errors[e];
                div = $('<div>');
                div.addClass('error');
                div.text(error);
                $console.append(div);
            }
        } else{
            // send ajax requests
            for(var i = 0; i < commands.length; i++){
                commandLine = commands[i].trim().split(' ');
                command = commandLine[0].toUpperCase();
                value = commandLine.length > 1 ? commandLine[1] : 'ON';

                if(command == 'WAIT'){
                    console.log('wait');
                } else {
                    url = 'http://' + curRobot.ip + '/?' + command + '=' + value;
                    ajaxSync(url);
                }
            }
        }
    }); 
    
    $console.keyup(function(evt){
        key = evt.key.toLowerCase();
        if(key == 'enter' || key == 'backspace' || key == 'delete'){
            updateConsoleLeft();
        }
    });
    
    updateConsoleLeft();
}

// send AJAX request
function sendRequest(command){
    if(allowRequest){
        allowRequest = false;
        var ip = curRobot.ip;
        url = 'http://' + ip + '/?' + command;
        
        console.log(url);
        $.get(url);
        
        // speed throttle
        setTimeout(function(){
            allowRequest = true;
        }, speedThrottle);
    }
}

function updateConsoleLeft(){
    $consoleLeft = $('#consoleLeft');
    rows = $console.text().split('\n').length - 1;
    rows = rows ? rows : 1;
    newText = ''
    for(var i = 0; i < rows; i++){
        space = (i + 1) <= 9 ? '  ' : '';
        newText += space + (i + 1) + ' | ' + curRobot.name + ' > ' + '\n';
    }
    $consoleLeft.attr('readonly', false);
    $consoleLeft.text(newText);
}
