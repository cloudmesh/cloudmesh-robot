var speedThrottle = 200;
var allowRequest = true;

var curRobot = {}

$(function(){    
    $robotSelect = $('#robotSelect');
    
    // create robot radio buttons
    $.each(fish['fish'], function(i, robot){
        var $p = $('<p>');
        var $radio = $('<input id="' + robot.name + '" type="radio" name="robots" value="' + robot.ip + '"/>');
        if(i == 0){
            $radio.attr('checked', 'checked');
            curRobot.ip = $radio.val();
        }
        var $label = $('<label for="' + robot.name + '">' + robot.name + '</label>');
        $p.append($radio);
        $p.append($label);
        $robotSelect.append($p);
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
    
    $readout = $('#readout');

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
