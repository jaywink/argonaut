"""The config model"""
from sqlalchemy import Column
from sqlalchemy.types import Unicode, UnicodeText

from argonaut.model.meta import Base, Session

class Config(Base):
    __tablename__ = 'config'

    id   = Column(Unicode(50), primary_key=True)
    value = Column(UnicodeText)
    
    def __init__(self, id=None, value=None):
        self.id = id
        self.value = value
    
    def __unicode__(self):
        return self.value
        
    def __repr__(self):
        return "<Config('%s','%s')>" % (self.id,self.value)

    __str__ = __unicode__
    
def get(id):
    return str(Session.query(Config).get(id).value)
