import os
import sys
from configparser import ConfigParser

from yfile import APP_HOME

def parser_config_file():
    """parser config file"""
    app_home = APP_HOME
    config_file = os.path.join(app_home, 'ifile.ini')

    if not os.path.exists(config_file):
        config_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'default_config.ini')
    
    config = ConfigParser()
    config.read(config_file)

    return config

config = parser_config_file()
core = config["core"]

SECRET_KEY = os.urandom(16)
SQLALCHEMY_DATABASE_URI=core["database_uri"]
STORAGE_TYPE = core["storage_type"]

if STORAGE_TYPE == "mongodb":
    mongodb = config["mongodb"]
    MONGO_URI = mongodb["uri"]
