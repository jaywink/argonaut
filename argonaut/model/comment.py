"""The comment model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, Date

from argonaut.model.meta import Base, Session

class Comment(Base):
    __tablename__ = 'comment'

    id   = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    body = Column(UnicodeText, nullable=False)
    posted = Column(Date, nullable=False)
    author = Column(Unicode(50), nullable=True)
    author_website = Column(Unicode(300), nullable=True)

    def __init__(self, id=None,post_id=None,body=None,posted=None,author=None,author_website=None):
        self.id = id
        self.post_id = post_id
        self.body = body
        self.posted = posted
        self.author = author
        self.author_website = author_website

    def __unicode__(self):
        return self.body
        
    def __repr__(self):
        return "<Comment('%s','%s', '%s', '%s', '%s', '%s')>" % (self.id,self.post_id,self.body,self.posted,self.author,self.author_website)

    __str__ = __unicode__
    
def new():
    return Comment()    
    
def save(comment):
    Session.add(comment)
    Session.commit()
        
def get_post_comments(post_id):
    return Session.query(Comment).filter_by(post_id=post_id).all()
    
def get_post_comment_count(id):
    return Session.query(Comment).filter_by(post_id=id).count()    
