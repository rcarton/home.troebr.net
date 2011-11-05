$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

function message(obj) {
	
	var form = $(obj).closest(".message-list-new");
	var value = form.children("textarea.value").val();
	var msg_list =  $(obj).closest(".message-list")
	var msg_list_name = msg_list.attr('id').substring('message-list-'.length);
	
	var url = '/ajax/add/message'
	
	if ($.trim(value) != "") {
		var data = { 
					 message_list: msg_list_name,
					 value: value
				   };
		
		$.ajax({
			  type: 'POST',
			  url: url,
			  data: data,
			  success: function(content) {
				  // Replace the message list
				msg_list.replaceWith(content);
			  }
			});
	}
}

/*
function message(e) {
    if (e.keyCode == 13) {
    	var url = '';
    	
    	var oreason = $("#BISOU_ADD_"+ user.toUpperCase() +"_REASON");
    	var reason =  oreason.val();
    	var amount =  oamount.val();
    	 
    	var data = {who: user,
    			reason: reason,
    			amount: amount}
    	$("#BISOU_ADD_"+ user.toUpperCase() +"_AMOUNT").blur();
    	
    	$.ajax({
    		  type: 'POST',
    		  url: url,
    		  data: data,
    		  success: function() {
    			  oreason.val("");
		    	  oamount.val("");
		    	  bisou_refresh(user);
    		  }
    		});
    }
}*/