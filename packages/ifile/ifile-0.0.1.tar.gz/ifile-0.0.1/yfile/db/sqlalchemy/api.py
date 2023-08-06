from datetime import datetime
from yfile.db.sqlalchemy.session import get_session
from yfile.db.sqlalchemy.models import YFilePicture, YFileGridFS
from yfile.exception import FileAlreadyExist, NotFound


def get_pictures():
    session = get_session()

    pictures = []

    with session.begin():
        results = session.query(YFilePicture, YFileGridFS). \
            filter(YFilePicture.yf_gridfs_id == YFileGridFS.id).all()

        for result in results:
            picture_db = result.YFilePicture
            catalogue_db = result.YFileGridFS

            picture = {
                "id": picture_db.id,
                "uuid": catalogue_db.uuid,
                "name": picture_db.name,
                "extension": picture_db.extension,
                "md5": catalogue_db.md5,
                "description": picture_db.description,
                "size": picture_db.size,
                "upload_date": catalogue_db.upload_date
            }
            pictures.append(picture)

        return pictures


def get_picture(id):
    session = get_session()
    with session.begin():
        item = session.query(YFilePicture, YFileGridFS). \
            filter(YFilePicture.id == id,
            YFilePicture.yf_gridfs_id == YFileGridFS.id).first()

        if not item:
            raise NotFound("picture not found, id: %s" % id)

        picture_db = item.YFilePicture
        catalogue_db = item.YFileGridFS

        picture = {
            "id": picture_db.id,
            "uuid": catalogue_db.uuid,
            "name": picture_db.name,
            "extension": picture_db.extension,
            "md5": catalogue_db.md5,
            "description": picture_db.description,
            "size": picture_db.size,
            "upload_date": catalogue_db.upload_date
        }

        return picture

def destory_picture(id):
    session = get_session()
    with session.begin():
        picture = session.query(YFilePicture).filter(
            YFilePicture.id == id
        ).first()

        if picture:
            session.query(YFilePicture).filter(
                YFilePicture.id == id).delete()
            session.query(YFileGridFS).filter(
                YFileGridFS.id == picture.yf_gridfs_id).delete()


def add_picture(name):
    picture = None
    extension = None
    if '.' in name:
        extension = name.split('.')[-1]

    session = get_session()
    with session.begin():
        gridfs = YFileGridFS()
        gridfs.save(session=session)

        picture = YFilePicture(
            name=name, extension=extension,
            yf_gridfs=gridfs)
        picture.save(session=session)

        return picture.id


def update_picture(id, **kwargs):
    chunk_size = kwargs.get('chunk_size')
    length = int(kwargs.get('length', 0))
    upload_date = kwargs.get('upload_date')
    uuid = kwargs.get('uuid')
    md5=kwargs.get('md5')
    object_id=kwargs.get('_id')

    session = get_session()
    with session.begin():
        result = session.query(YFilePicture, YFileGridFS).filter(
            YFilePicture.id == id, YFileGridFS.id == YFilePicture.yf_gridfs_id).first()
        picture = result.YFilePicture
        gridfs = result.YFileGridFS

        gridfs.update(
            uuid=uuid, md5=md5,
            object_id=str(object_id),
            chunk_size=chunk_size,
            length=length,
            upload_date=upload_date)

        gridfs.save(session=session)

        picture.update(size=length / 1024)
        picture.save(session=session)

        return picture
