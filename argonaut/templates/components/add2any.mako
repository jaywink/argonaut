
<%def name="button(title,link)">\
    <!-- AddToAny BEGIN -->
    <a class="a2a_dd" href="http://www.addtoany.com/share_save?linkurl=${link}&amp;linkname=${title}"><img src="http://static.addtoany.com/buttons/share_save_171_16.png" width="171" height="16" border="0" alt="Share/Bookmark"/></a>
    <script type="text/javascript">
        % if c.counter_post_on_page == 1:
            var a2a_config = a2a_config || {};
        % endif
        a2a_config.linkname = "${title}";
        a2a_config.linkurl = "${link}";
        a2a_config.no_3p=1;
        <%
            context.write('a2a_config.templates = {twitter: "'+chr(36)+'{title} - '+chr(36)+'{link}"};')
        %>
    </script>
    % if c.counter_post_on_page == 1:
        <script type="text/javascript" src="http://static.addtoany.com/menu/page.js"></script>
    % else:
        <script type="text/javascript">
        a2a.init('page');
        </script>
    % endif
    <!-- AddToAny END -->
</%def>


