"""The box model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Unicode, Integer

from argonaut.model.meta import Base, Session

class Box(Base):
    __tablename__ = 'box'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), unique=True, nullable=False)
    template = Column(Unicode(30), nullable=False)
    
    def __init__(self, id=None, name=None, template=None):
        self.id = id
        self.name = name
        self.template = template
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Box('%s','%s','%s')>" % (self.id,self.name, self.template)

    __str__ = __unicode__
    
def get(id):
    return Session.query(Box).filter(Box.id == id).one()
