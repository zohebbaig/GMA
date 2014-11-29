$(document).ready(function() {

    // QUERY NEW MESSAGES CONTINUOUSLY
    (function message_retriever() {
        $.ajax({
            url: '/ajax/messages/',
            data: {user_id: $('#uid').val()},
            success: function(data){
                $('#messaging_div').html(data);
            },
            complete: function() {
                setTimeout(message_retriever, 1000);
            }
        });
    })();

    // OVERRIDE BROWSER DEFAULT POST SUBMIT FOR MESSAGING
    $('#message_form').on('submit', function(event){
        event.preventDefault();
        var msg_data={
            message: $('#message_text').val(),
            user_id: $('#uid').val(),
            csrfmiddlewaretoken: getCookie('csrftoken')
        }
        $.post('/ajax/send_user_msg/',msg_data)
        $('#messaging_div').slimScroll({ scrollTo : 0 });
        $('#message_text').val('');
    });

    // SOURCE: Django docs https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/
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
