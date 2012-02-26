"""The page_type model"""

from pylons import request, response, session, tmpl_context as c, url
from sqlalchemy import Column
from sqlalchemy.types import Unicode, Integer
from argonaut.model.meta import Base, Session

class Page_Type(Base):
    __tablename__ = 'page_type'

    id   = Column(Integer, primary_key=True)
    name = Column(Unicode(30), nullable=False)
    controller = Column(Unicode(30), nullable=True)
    action = Column(Unicode(30), nullable=True)
    param = Column(Unicode(30), nullable=True)
    
    def __init__(self):
        self.id = None
        self.name = ''
        self.controller = None
        self.action = None
        self.param = None
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Page_Type('%s','%s','%s','%s','%s')>" % (self.id,self.name,self.controller,self.action,self.param)

    __str__ = __unicode__

def get_url(id, url_param):
    route = Session.query(Page_Type).get(id)
    if url_param:
        target = url(controller=route.controller, action=route.action, id=url_param)
    elif len(route.param) > 0:
        target = url(controller=route.controller, action=route.action, id=route.param)
    else:
        target = url(controller=route.controller, action=route.action)
    return target
