$(document).ready(function() {

    // slimscroll is a jQuery pluging which enables a scrollable div, $ refers to an ID
    // source: http://rocha.la/jQuery-slimScroll
    $(function(){
        $('#messaging_div').slimScroll({
            height: '200px',
            start: 'top'
        });
    });

    // Swap label/icon on messaging drop-down, dynamic to change drop down icon for show/hide
    $(function(){
        $('#messaging_collapse').on('hide.bs.collapse', function () {
            $('#toggle-button').html('<span class="glyphicon glyphicon-collapse-down"></span> Show Chat');
        })
        $('#messaging_collapse').on('show.bs.collapse', function () {
            $('#toggle-button').html('<span class="glyphicon glyphicon-collapse-up"></span> Hide Chat');
        })
    })
    $(function(){
        $('#members_collapse').on('hide.bs.collapse', function () {
            $('#toggle-button-members').html('<span class="glyphicon glyphicon-collapse-down"></span> Show Members');
        })
        $('#members_collapse').on('show.bs.collapse', function () {
            $('#toggle-button-members').html('<span class="glyphicon glyphicon-collapse-up"></span> Hide Members');
        })
    })

    // These are modifications of the examples in tango with django, input box, searching for key events, #refers to ID
    //user search
    $('#s_fn').keyup(function(){
        $.get('/ajax/user_search/', {first_name: $('#s_fn').val(), last_name: $('#s_ln').val()}, function(data){
            $('#search_results').html(data);
        });
    });

    $('#s_ln').keyup(function(){
        $.get('/ajax/user_search/', {first_name: $('#s_fn').val(), last_name: $('#s_ln').val()}, function(data){
            $('#search_results').html(data);
        });
    });

//group search
    $('#s_group').keyup(function(){
        $.get('/ajax/group_search/', {group_name: $('#s_group').val()}, function(data){
            $('#search_results').html(data);
        });
    });


});