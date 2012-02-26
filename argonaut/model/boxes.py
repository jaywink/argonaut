"""The boxes model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer

from argonaut.model.meta import Base, Session

class Boxes(Base):
    __tablename__ = 'boxes'

    id = Column(Integer, primary_key=True)
    box_id = Column(Integer, ForeignKey('box.id'), nullable=False)
    status = Column(Integer, default = 1)
    order = Column(Integer, unique=True, nullable=False)
    
    def __init__(self, id=None, box_id=None, status=None, order=None):
        self.id = id
        self.box_id = box_id
        self.status = status
        self.order = order
    
    def __unicode__(self):
        return self.box_id
        
    def __repr__(self):
        return "<Boxes('%s','%s','%s','%s')>" % (self.id,self.box_id,self.status,self.order)

    __str__ = __unicode__
    
def get_all():
    return Session.query(Boxes).filter(Boxes.status == 1).order_by(Boxes.order.asc()).all()
