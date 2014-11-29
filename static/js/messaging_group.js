$(document).ready(function() {

    // QUERY NEW MESSAGES CONTINUOUSLY, gets new messages continuously, AJAX get method from JQuery, infinite loop
    (function message_retriever() {
        $.ajax({
            url: '/ajax/messages/',
            data: {group_id: $('#gid').val()},
            success: function(data){
                $('#messaging_div').html(data);
            },
            complete: function() {
                setTimeout(message_retriever, 1000);
            }
        });
    })();

    // OVERRIDE BROWSER DEFAULT POST SUBMIT FOR MESSAGING, if press enter, doesnt do default, call method to get message text
    // csrf cross-site request forgery token from the template, gets a unique hash token and send to post request, security feature
    // post request not default, sets slimscroll to the top to show latest messages, clear send message to input box
    $('#message_form').on('submit', function(event){
        event.preventDefault();
        var msg_data={
            message: $('#message_text').val(),
            group_id: $('#gid').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        }
        $.post('/ajax/send_grp_msg/',msg_data)
        $('#messaging_div').slimScroll({ scrollTo : 0 });
        $('#message_text').val('');
    });

    // SOURCE: Django docs https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/
    // Django documentation code for cookie handling, used for getting token
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

});


