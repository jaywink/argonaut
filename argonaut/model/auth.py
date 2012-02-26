"""The auth model

Thanks to http://sarafsaurabh.wordpress.com/2010/08/10/pylons-authentication-and-authorization-using-repoze-what/
for repoze.what related authentication and code in this model

"""
import os
from hashlib import sha1

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Unicode, Integer
from sqlalchemy.orm import relation

from argonaut.model.meta import Base, Session

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(30), unique=True, nullable=False)
    email = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(80), nullable=False)
    name = Column(Unicode(255), nullable=False)
    
    def __init__(self, id=None, username=None, email=None, password=None, name=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.name = name
    
    def __unicode__(self):
        return self.username
        
    def __repr__(self):
        return "<User('%s','%s','%s','%s','%s')>" % (self.id,self.username, self.email, self.password, self.name)

    __str__ = __unicode__
    
    groups = relation('Group', secondary='user_group')
    
    def _set_password(self, password):
        """Hash password on the fly."""
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        # Make sure the hased password is an UTF-8 object at the end of the
        # process because SQLAlchemy _wants_ a unicode object for Unicode
        # fields
        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')

        self.password = hashed_password

    def _get_password(self):
        """Return the password hashed"""
        return self.password

    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Group('%s','%s')>" % (self.id,self.name)

    __str__ = __unicode__
    
    permissions = relation('Permission', secondary='group_permission')
    users = relation('User', secondary='user_group')

class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def __unicode__(self):
        return self.name
        
    def __repr__(self):
        return "<Permission('%s','%s')>" % (self.id,self.name)

    __str__ = __unicode__
    
    groups = relation('Group', secondary='group_permission')
    
class Group_Permission(Base):
    __tablename__ = 'group_permission'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))
    
    def __init__(self):
        pass
        
    def __unicode__(self):
        return self.group_id
        
    def __repr__(self):
        return "<Group_Permission('%s','%s','%s')>" % (self.id,self.group_id,self.permission_id)

    __str__ = __unicode__   
    
class User_Group(Base):
    __tablename__ = 'user_group'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    
    def __init__(self):
        pass
        
    def __unicode__(self):
        return self.user_id
        
    def __repr__(self):
        return "<User_Group('%s','%s','%s')>" % (self.id,self.user_id,self.group_id)

    __str__ = __unicode__   
        
def get_user_name(username=None, id=None):
    if username:
        return Session.query(User).filter(User.username == username).first().name
    if id:
        return Session.query(User).filter(User.id == id).first().name
            
def get_user_mail(id):
    try:
        return Session.query(User).filter(User.id == id).first().email  
    except AttributeError:
        return None
    
def get_user_id(username):
    return Session.query(User).filter(User.username == username).first().id        
    
