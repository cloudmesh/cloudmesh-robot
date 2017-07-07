/*$(function(){
    // min/max duty on robot motors
    var minValue = 0;
    var maxValue = 90;
    
    // slider stepping
    var step = 10;
    
    // limit number of requests (milliseconds between each request)
    var speedThrottle = 200;
    var allowRequest = true;

    // currently selected robot
    var curRobot = {
        speedLeft: minValue,
        speedRight: minValue,
        ip: ''
    };
    
    var directionMultiplier = [1,1];
    
    var $rightMeter = $("#rightMeter").dynameter({
    	width: 200,
    	label: 'Fin Right',
    	value: minValue,
    	min: minValue,
    	max: maxValue,
    	unit: 'Angle'
    });
    
    var $leftMeter = $("#leftMeter").dynameter({
    	width: 200,
    	label: 'Fin Left',
    	value: minValue,
    	min: minValue,
    	max: maxValue,
    	unit: 'Angle'
    });
    
    $('#terminate').click(function(){
        terminate();
    });
    
    // call reset to initiate sliders
    resetValues();
    
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
    
    // button clicked
    $('#keys li').click(function(){        
        index = $(this).index();
        switch(index){
            case 0:
                directionMultiplier = [1,1];
                break;
            case 1:
                directionMultiplier = [1,-1];
                break;
            case 2:
                directionMultiplier = [0,0];
                break;                
            case 3:
                directionMultiplier = [-1,1];
                break;
            case 4:
                directionMultiplier = [-1,-1];
                break;
        }
        
        sendRequest();
    });
    
    // new robot selected
    $('input[type=radio][name=robots]').change(function() {
        resetValues();
        terminate();
        curRobot.speedLeft = minValue;
        curRobot.speedRight = minValue;
        curRobot.ip = $(this).val();             
    });
    
    // send AJAX request
    function sendRequest(){
        if(allowRequest){
            allowRequest = false;
            var ip = curRobot.ip;
            url = 'http://' + ip + '/?LEFT=' + curRobot.speedLeft * directionMultiplier[0] + '&RIGHT=' + curRobot.speedRight * directionMultiplier[1];
            
            console.log(url);
            $.get(url);
            
            // speed throttle
            setTimeout(function(){
                allowRequest = true;
            }, speedThrottle);
        }
    }
    
    // change all values to 0
    function resetValues(){
        directionMultiplier = [0,0];
        sendRequest();
        
        $rightMeter.changeValue(minValue);
        $leftMeter.changeValue(minValue);
    
        $('#leftSlider').slider({
        	min: minValue,
        	max: maxValue,
        	value: minValue,
        	step: step,
        	slide: function(evt, ui) {
        		$leftMeter.changeValue(ui.value);
        		curRobot.speedLeft = ui.value;
        	}
        });
        
        $('#rightSlider').slider({
        	min: minValue,
        	max: maxValue,
        	value: minValue,
        	step: step,
        	slide: function(evt, ui) {
        		$rightMeter.changeValue(ui.value);
        		curRobot.speedRight = ui.value;
        	}
        });
    }
    
    function terminate(){
        directionMultiplier = [0,0];
        sendRequest();
        
        var ip = curRobot.ip;
        url = 'http://' + url + '/?END=1';
        $.get(url);
    }
});*/

$(function(){
    var maxValue = 180;
 
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
    gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
    gauge.animationSpeed = 1; // set animation speed (32 is default value)
    gauge.set(90); // set actual value
    
    var clicked = false;
    var gaugeWidth = gauge.canvas.clientWidth;
    
    $('#finGauge').mousedown(function(){
        clicked = true;
    }).mouseup(function(){
        clicked = false;
    }).mousemove(function(evt){
        if(clicked){
            clickX = evt.offsetX;
            gauge.set((clickX / gaugeWidth) * gaugeWidth);
            console.log(gauge.value);
        }
    });
});
