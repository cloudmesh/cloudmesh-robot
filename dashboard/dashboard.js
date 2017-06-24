var $myRightMeter, $myLeftMeter;
$(function(){
    // limit number of requests (milliseconds between each request)
    var speedThrottle = 200;
    var allowRequest = true;
    var lastSpeedSent = {}

    // speed obj to store speed for http requests
    var speedObj = {left: 0, right: 0};
    
    // currently selected robot
    var curRobot = null;
    
    $myRightMeter = $("div#rightMeterDiv").dynameter({
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
    
    $myLeftMeter = $("div#leftMeterDiv").dynameter({
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
    
    resetValues();
    
    $form = $('#formDiv');
    
    $.each(robots['robots'], function(i, robot){
        var $radio = $('<input type="radio" name="robots" value="' + robot.ip + '"/>');
        if(i == 0){
            $radio.attr('checked', 'checked');
            curRobot = $radio;
        }
        var $label = $('<label>' + robot.name + '</label>');
        $form.append($radio);
        $form.append($label);
    });
    
    // new robot selected
    $('input[type=radio][name=robots]').change(function() {
        curRobot = $(this);
        speedObj.left = 0;
        speedObj.right = 0;
        updateSpeeds();                
        resetValues();
    });
    
    // send AJAX request
    function updateSpeeds(){
        if(allowRequest){
            allowRequest = false;
            var url = curRobot.val();
            url = 'http://' + url + '?left=' + speedObj.left + '&right=' + speedObj.right;
            console.log(url);
            //$.get(url);
            lastSpeedSent.right = speedObj.right;
            lastSpeedSent.left = speedObj.left;
            setTimeout(function(){
                allowRequest = true;
                if(lastSpeedSent.right != speedObj.right || lastSpeedSent.left != speedObj.left){
                    updateSpeeds();
                }
            }, speedThrottle);
        }
    }
    
    // change all values to 0
    function resetValues(){
        $myRightMeter.changeValue(0);
        $myLeftMeter.changeValue(0);
    
        $('div#leftSliderDiv').slider({
        	min: 0,
        	max: 1023,
        	value: 0,
        	step: 10,
        	slide: function (evt, ui) {
        		$myLeftMeter.changeValue(ui.value);
        		speedObj.left = ui.value;
        		updateSpeeds();
        	}
        });
        
        $('div#rightSliderDiv').slider({
        	min: 0,
        	max: 1023,
        	value: 0,
        	step: 10,
        	slide: function (evt, ui) {
        		$myRightMeter.changeValue(ui.value);
        		speedObj.right = ui.value;
        		updateSpeeds();
        	}
        });
    }
});
