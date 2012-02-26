"""The social model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Unicode, Integer

from argonaut.model.meta import Base, Session

class Social(Base):
    __tablename__ = 'social'

    id   = Column(Integer, primary_key=True)
    name = Column(Unicode(30), nullable=False)
    status = Column(Integer, default = 1)
    priority = Column(Integer, nullable=False, default=50)
    url = Column(Unicode(500), nullable=False)
    media_id = Column(Integer, ForeignKey('media.id'), nullable=True)
    
    def __init__(self, id=None, name=None, status=1, priority=None, url=None, media_id=None):
        self.id = id
        self.name = name
        self.status = status
        self.priority = priority
        self.url = url
        self.media_id = media_id
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Page('%s','%s','%s','%s','%s','%s')>" % (self.id,self.name,self.status,self.priority,self.url,self.media_id)

    __str__ = __unicode__
    
def get_name(id):
    return str(Session.query(Social).get(id).name)
    
def get_all():
    return Session.query(Social).order_by(Social.priority).all()    

def get_active():
    return Session.query(Social).filter(Social.status == 1).order_by(Social.priority).all() 
    
def get_first():
    return Session.query(Social).order_by(Social.priority).first()
    
def get_url(id):
    return Session.query(Social).get(id).url
