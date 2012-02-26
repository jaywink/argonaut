"""The page model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Unicode, Integer

from argonaut.model.meta import Base, Session

class Page(Base):
    __tablename__ = 'pages'

    id   = Column(Integer, primary_key=True)
    name = Column(Unicode(30), nullable=False)
    status = Column(Integer, default = 1)
    page_order = Column(Integer, nullable=False, default=50)
    url = Column(Unicode(200), nullable=True)
    url_param = Column(Unicode(80), nullable=True)
    page_type_id = Column(Integer, ForeignKey('page_type.id'), nullable=False)
    parent_id = Column(Integer, nullable=True)
    
    def __init__(self, id=None, name=None, status=1, page_order=None, url=None, url_param=None, page_type_id=1, parent_id=None):
        self.id = id
        self.name = name
        self.status = status
        self.page_order = page_order
        self.url = url
        self.page_type_id = page_type_id
        self.url_param = url_param
        self.parent_id = parent_id
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Page('%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.id,self.name,self.status,self.page_order,self.url,self.page_type_id,self.url_param,self.parent_id)

    __str__ = __unicode__
    
def get_title(id):
    from argonaut.model.config import Config
    return str(Session.query(Page).get(id).name.encode('utf8'))+' ['+str(Session.query(Config).get('site_title').value)+']'
    
def generate_title(name):
    from argonaut.model.config import Config
    return name+' ['+str(Session.query(Config).get('site_title').value)+']' 
    
def get_name(id):
    return str(Session.query(Page).get(id).name)
    
def get_all():
    return Session.query(Page).order_by(Page.page_order).all()    
    
def get_active():
    return Session.query(Page).filter(Page.status==1).order_by(Page.page_order).all()    
    
def get_first():
    return Session.query(Page).order_by(Page.page_order).first()
    
def get_page_id_with_type(type):
    from argonaut.model.page_type import Page_Type
    return int(Session.query(Page).join(Page_Type).filter(Page_Type.name==type).order_by(Page.id.desc()).first().id)
    
def get_url(id):
    return Session.query(Page).get(id).url
    
def get_page_type_id(id):
    return Session.query(Page).get(id).page_type_id

def get_url_param(id):
    return Session.query(Page).get(id).url_param
    
def get_id_by_url_param(url_param):
    return Session.query(Page).filter(Page.url_param == url_param).first().id
    
def get_id_by_type_param(param):
    from argonaut.model.page_type import Page_Type
    return int(Session.query(Page).join(Page_Type).filter(Page_Type.param==param).order_by(Page.id.desc()).first().id)
