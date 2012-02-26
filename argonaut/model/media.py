"""The media model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Unicode, Integer

from argonaut.model.meta import Base, Session

class Media(Base):
    __tablename__ = 'media'

    id   = Column(Integer, primary_key=True)
    name = Column(Unicode(30), nullable=False)
    url = Column(Unicode(500), nullable=False)
    
    def __init__(self, id=None, name=None, url=None):
        self.id = id
        self.name = name
        self.url = url
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Page('%s','%s','%s')>" % (self.id,self.name,self.url)

    __str__ = __unicode__

def get(id):
    return Session.query(Media).get(id)
    
def get_name(id):
    return str(Session.query(Media).get(id).name)
    
def get_all():
    return Session.query(Media).all()    
    
def get_first():
    return Session.query(Media).first()
    
def get_url(id):
    return Session.query(Media).get(id).url

