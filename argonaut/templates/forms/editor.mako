<%namespace name="tags_list" file="/blog/tags_list.mako" />

<%def name="editor_form(post)">
    ${h.javascript_link('/ckeditor/ckeditor.js')}
    ${h.javascript_link('/js/editor.js')}
    %if c.post is None:
        <% id = 0 %>
    %else:
        <% id = c.post.id %>
    %endif
    ${h.form(h.url(controller='blog', action='save', id=id), method='post', id='editor_form')}
    ## subject
    <p>Subject<br>${h.text('subject', class_='full_width')}
    ## body
    <p>${h.textarea('body')}</p>
    <script type="text/javascript">
        CKEDITOR.replace('body');
    </script>
    ## tags
    <p>Add tags separated by a semicolon (;)
    <%
        number_of_tags = h.tag.get_number_of_tags()
    %>
    %if number_of_tags > 0:
         and/or select some existing ones from below
        <%
            ## get list of tags
            tags = h.tag_post.get_tag_counts()
        %>
    %endif
    <br>${h.text('tags', class_='full_width', id='tags')}
    </p>
    %if number_of_tags > 0:
        ${tags_list.list_as_links_for_editor(tags)}
    %endif
    ## submit
    <p>${h.submit('submit', 'Submit')}</p>
    ${h.end_form()}
    %if id > 0:
        ## once page has loaded, toggle tags that are preselected if editing post
        <script type="text/javascript">
            $(document).ready(function() {
                toggleAllTags(document.getElementById('tags').value);
            });
        </script>
    %endif
</%def>
