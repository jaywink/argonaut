${h.form(h.url(controller='blog', action='archives'), method='get')}
<p><div class="no_overflow">${h.text('filter', size=30)} ${h.submit('submit', 'Filter')}</div></p>
${h.end_form()}
