$(function(){
    // min/max duty on robot motors
    var minValue = 700;
    var maxValue = 1023;
    
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
    	label: 'Right',
    	value: minValue,
    	min: minValue,
    	max: maxValue,
    	unit: 'Speed',
    	regions: {
    		870: 'warn',
    		950: 'error'
    	}
    });
    
    var $leftMeter = $("#leftMeter").dynameter({
    	width: 200,
    	label: 'Left',
    	value: minValue,
    	min: minValue,
    	max: maxValue,
    	unit: 'Speed',
    	regions: {
    		870: 'warn',
    		950: 'error'
    	}
    });
    
    $('#terminate').click(function(){
        terminate();
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
    
    $(document).keydown(function(evt){
        evt.preventDefault();
        index = -1;
        switch(evt.key){
            case 'ArrowUp':
                index = 0;
                break;
            case 'ArrowLeft':
                index = 1;
                break;
            case ' ':      
            case 'Escape':
                index = 2;
                break;
            case 'ArrowRight':
                index = 3;
                break;
            case 'ArrowDown':
                index = 4;
                break;
        }
        
        if(index == -1){
            return;
        }
        
        $key = $('#keys').children().eq(index);
        $key.trigger('click');
        $key.addClass('pressed');
        
        setTimeout(function(){
            $key.removeClass('pressed');
        }, 200);
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
});
