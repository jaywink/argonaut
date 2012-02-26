import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from argonaut.lib.base import BaseController, render

import argonaut.lib.helpers as h
from webhelpers.feedgenerator import Rss201rev2Feed

log = logging.getLogger(__name__)

class FeedController(BaseController):

    def posts(self):
        posts = h.post.get_many(amount=10, active_only=True, order='desc')
        feed = Rss201rev2Feed(
            title=h.config.get('rss_title'),
            link=h.config.get('site_url'),
            description=h.config.get('rss_title'),
            language=u"en")
        for p in posts:
            link = h.config.get('site_url')+h.escape(h.url('blog_post', id=p.id, subject=h.urlify(p.subject)))
            tags = h.tag_post.get_tags(p.id)
            tags_list = []
            for tag in tags:
                tags_list.append(tag.name)
            feed.add_item(title=p.subject, link=link, description=p.body, pubdate=p.posted, unique_id=str(p.id), categories=tags_list)
        response.content_type = 'application/rss+xml'
        return feed.writeString('utf-8')
