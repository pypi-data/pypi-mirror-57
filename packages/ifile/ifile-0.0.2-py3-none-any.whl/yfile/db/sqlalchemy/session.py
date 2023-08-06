from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import current_app


def get_engine(echo=False):
    engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"],
                           echo=echo)
    return engine


def get_session(autocommit=True):
    engine = get_engine()
    session = sessionmaker(bind=engine, autocommit=autocommit)
    return session()
