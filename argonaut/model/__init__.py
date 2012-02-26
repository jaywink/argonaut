"""The application's model objects"""
from argonaut.model.meta import Session, Base

from argonaut.model.post import Post
from argonaut.model.config import Config
from argonaut.model.page_type import Page_Type
from argonaut.model.page import Page
from argonaut.model.box import Box
from argonaut.model.boxes import Boxes
from argonaut.model.tag import Tag
from argonaut.model.tag_post import Tag_Post
from argonaut.model.comment import Comment
from argonaut.model.media import Media
from argonaut.model.social import Social
from argonaut.model.auth import User, Group, Permission, User_Group, Group_Permission

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
    

