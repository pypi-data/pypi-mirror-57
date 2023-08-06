from datetime import datetime

from sqlalchemy import (
    Column, Integer, String,
    DateTime, Text, ForeignKey,
    Boolean)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from yfile.db.sqlalchemy.session import get_session

Base = declarative_base()
metadata = Base.metadata


class MetaBase(object):
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), server_default=func.now())

    def save(self, session=None):
        if session is None:
            session = get_session()
            with session.begin():
                session.add(self)
        else:
            session.add(self)
            session.flush()

    def update(self, **kwargs):
        self.update_at = func.now()

        for k, v in kwargs.items():
            setattr(self, k, v)


class YFilePicture(Base, MetaBase):
    __tablename__ = 'yf_picture'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    size = Column(Integer)
    label = Column(String(60))
    extension = Column(String(10))
    is_process = Column(Boolean())
    description = Column(Text())
    shooting_time = Column(DateTime())

    yf_gridfs = relationship("YFileGridFS", back_populates="yf_picture")
    yf_gridfs_id = Column(Integer, ForeignKey('yf_gridfs.id'))


class YFileGridFS(Base, MetaBase):
    __tablename__ = 'yf_gridfs'

    id = Column(Integer, primary_key=True)
    object_id = Column(String(100))
    uuid = Column(String(100))
    md5 = Column(String(100))
    chunk_size = Column(Integer)
    length = Column(Integer)
    upload_date = Column(DateTime(timezone=True))

    yf_picture = relationship("YFilePicture", uselist=False,
                              back_populates="yf_gridfs")
