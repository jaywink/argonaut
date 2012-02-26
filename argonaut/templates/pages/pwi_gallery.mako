<%inherit file="/base.mako"/>\

<%def name="title()">\
    ${h.page.get_title(page_id)}
</%def>

## Content starts here

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script> 

<link href="/jquery.pwi/css/pwi.css" rel="stylesheet" type="text/css"/> 
<link href="/jquery.pwi/js/jquery.slimbox2/jquery.slimbox2.css" rel="stylesheet" type="text/css"/> 
<script src="/jquery.pwi/js/jquery.pwi.js" type="text/javascript"></script>

<script src="/jquery.pwi/js/jquery.blockUI.js" type="text/javascript"></script>
<script src="/jquery.pwi/js/jquery.slimbox2/jquery.slimbox2.js" type="text/javascript"></script>

<script type="text/javascript">
    $(document).ready(function() {  //-- default jQuery call, do stuff when page is loaded
        var options = {
            // EDIT / ADD OPTIONS:
            // see page pwi page http://code.google.com/p/pwi/wiki/HowTo for instructions on options
            //--REPLACE WITH YOUR PICASA NAME!!!! (see the url when visiting your albums at google, you notice it right after the domain. It's NOT your username by default!!!
            username: 'usernamehere'
        };
        $("#pwi_gallery").pwi(options);
    });
</script>

<p><h1>${h.page.get_name(page_id)}</h1></p>

<p><div id="pwi_gallery">

</div></p>
