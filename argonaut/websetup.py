"""Setup the argonaut application"""
import logging

import pylons.test

from argonaut.config.environment import load_environment
from argonaut.model.meta import Session, Base
from argonaut.model.initial_data import config_data, page_data, auth_data, box_data, boxes_data, page_type_data, media_data, social_data

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """
    
    To set up the application, you need to use the command:
    paster setup-app <config_file>:#arg
    
    This is due to a bug in pastedeploy (http://www.mail-archive.com/pylons-discuss@googlegroups.com/msg08524.html)
    
    """
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)

    # Load initial data
    config_data.init_data()
    page_type_data.init_data()
    page_data.init_data()
    auth_data.init_data()
    box_data.init_data()
    boxes_data.init_data()
    media_data.init_data()
    social_data.init_data()
    
