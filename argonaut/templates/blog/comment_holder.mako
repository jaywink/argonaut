% for comment in comments:
    <p><span class="author">${comment.author}</span> (<span class="posted">${comment.posted.strftime('%c')}</span>)<br><span class="body">${h.auto_link(h.literal(comment.body))}</span></p>
% endfor
