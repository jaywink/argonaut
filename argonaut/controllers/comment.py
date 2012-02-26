import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

import argonaut.lib.helpers as h
from argonaut.lib.base import BaseController, render

from formencode import htmlfill

log = logging.getLogger(__name__)

class CommentController(BaseController):
    
    def get_all(self, id):
        comments = h.comment.get_post_comments(id)
        return render('/blog/comment_holder.mako', extra_vars={'comments':comments})
    
    def submit(self):
        c.post = h.post.get(int(request.params.get('post_id')))
        c.posts = None
        if h.forms.validate(h.forms.CommentForm()):         
            # save comment
            comment = h.comment.new()
            for k, v in c.form_result.items():
                setattr(comment, k, v)
            # some checks and defaults
            if len(comment.author) == 0:
                comment.author = 'anonymous'
            comment.posted = h.timehelpers.now()
            comment.body = h.html_escape(comment.body)
            comment.body = comment.body.replace('\n','<br>')
            comment.body = comment.body.replace('\t','&nbsp;')
            comment.body = comment.body.replace('  ','&nbsp; ')
            # save to db
            h.comment.save(comment)
            # flash message
            session['flash'] = 'Comment successfully saved.'
            session.save()
            # notify author
            h.mailer.send_mail('argonaut@basshero.org', h.auth.get_user_mail(c.post.author), 'New comment for: '+c.post.subject, render('/messages/mail_new_comment.mako', extra_vars={'user':h.auth.get_user_name(id=c.post.author), 'post_subject':c.post.subject, 'site_name':h.config.get('site_title'), 'post_url':h.config.get('site_url')+url(controller='blog', action='view', id=c.post.id, subject=h.urlify(c.post.subject))}))
            # redirect to post
            redirect(url(controller='blog', action='view', id=request.params.get('post_id'), subject=h.urlify(c.post.subject)), code=303)
        else:
            session['flash'] = 'Erros in the submitted form, please correct and try again.'
            session.save()
            html = render('/blog/view.mako', extra_vars={'page_id':1, 'post_count':1})
            return htmlfill.render(html,defaults=c.form_result,errors=c.form_errors)



