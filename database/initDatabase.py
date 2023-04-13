from db import engine
from sqlalchemy import MetaData

from models.models import Task

if __name__ == '__main__':
    metadata_obj = MetaData()
    metadata_obj.create_all(engine, tables=[Task.__table__])
