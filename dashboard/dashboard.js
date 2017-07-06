$(function(){
    // limit number of requests (milliseconds between each request)
    var speedThrottle = 200;
    var allowRequest = true;

    // currently selected robot
    var curRobot = {
        speedLeft: 0,
        speedRight: 0,
        ip: ''
    };
    
    var directionMultiplier = [1,1];
    
    var $rightMeter = $("#rightMeter").dynameter({
    	width: 200,
    	label: 'Right',
    	value: 0,
    	min: 0,
    	max: 1023,
    	unit: 'Speed',
    	regions: {
    		800: 'warn',
    		900: 'error'
    	}
    });
    
    var $leftMeter = $("#leftMeter").dynameter({
    	width: 200,
    	label: 'Left',
    	value: 0,
    	min: 0,
    	max: 1023,
    	unit: 'Speed',
    	regions: {
    		800: 'warn',
    		900: 'error'
    	}
    });
    
    // call reset to initiate sliders
    resetValues();
    
    $robotSelect = $('#robotSelect');
    
    // create robot radio buttons
    $.each(robots['robots'], function(i, robot){
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
                directionMultiplier = [-1,1];
                break;
            case 2:
                directionMultiplier = [0,0];
                break;                
            case 3:
                directionMultiplier = [1,-1];
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
        curRobot.speedLeft = 0;
        curRobot.speedRight = 0;
        curRobot.ip = $(this).val();             
    });
    
    // send AJAX request
    function sendRequest(){
        if(allowRequest){
            allowRequest = false;
            var url = curRobot.ip;
            url = 'http://' + url + '?left=' + curRobot.speedLeft * directionMultiplier[0] + '&right=' + curRobot.speedRight * directionMultiplier[1];
            
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
        
        $rightMeter.changeValue(0);
        $leftMeter.changeValue(0);
    
        $('#leftSlider').slider({
        	min: 0,
        	max: 1023,
        	value: 0,
        	step: 10,
        	slide: function(evt, ui) {
        		$leftMeter.changeValue(ui.value);
        		curRobot.speedLeft = ui.value;
        	}
        });
        
        $('#rightSlider').slider({
        	min: 0,
        	max: 1023,
        	value: 0,
        	step: 10,
        	slide: function(evt, ui) {
        		$rightMeter.changeValue(ui.value);
        		curRobot.speedRight = ui.value;
        	}
        });
    }
});
