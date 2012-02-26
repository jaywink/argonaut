// anti-spam idea from http://gatekiller.co.uk/Post/JavaScript_Captcha  (c) Stephen Hill
var antiSpam = function() {
    var localCounter = 0;
    if (document.getElementById("antiSpam")) {
        var a = document.getElementById("antiSpam");
        var button = document.getElementById("comment_submit");
        if (isNaN(a.value) == true) {
                a.value = 0;
        } else {
            a.value = parseInt(a.value) + 1;
            localCounter = a.value;
            // submit button is disabled by default. when countdown is finished, enable it
            if (a.value == 3) {
                $('input[type="submit"]').removeAttr('disabled');
            }
        }
    }
    var counter = setTimeout("antiSpam()", 1000);
    // cancel counting after time has passed
    if (localCounter > 3) {
        clearTimeout(counter);
    }
}
antiSpam();

function Post() {

    this.init = function(post_id,page) {
        $('#post_comment_'+post_id).hide();
        if (page != 'view') {
            $('#ajax_loading_'+post_id).hide();
        }
        $('a.comment_form_expand_'+post_id).click(function() {
            $('#post_comment_'+post_id).slideToggle('fast');
        });
        if (page == 'view') {
            $.get('/comment/get_all/'+post_id, function(data) {
                $('#comments_holder_'+post_id).html(data);
                $('#ajax_loading_'+post_id).hide();
            });
        }
        $('a.comments_show_'+post_id).click(function() {
            $('#ajax_loading_'+post_id).show();
            $.get('/comment/get_all/'+post_id, function(data) {
                $('#comments_holder_'+post_id).html(data);
                $('#ajax_loading_'+post_id).hide();
            });
        });
    }
    
}

