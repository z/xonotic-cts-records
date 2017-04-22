from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import MetaData

from xcr.base import Base
from xcr.util import database


class Session(Base):

    def __init__(self):
        super().__init__()

        # setup db
        db_path = self.conf.get('database', 'sqlite:///xcr.db')
        self.db_engine = create_engine(db_path)
        self.db_factory = sessionmaker(bind=self.db_engine)
        self.db_session = scoped_session(self.db_factory)
        self.db_metadata = MetaData()
        self.db_base = declarative_base(metadata=self.db_metadata, bind=self.db_engine)
        self.db = self.db_session()

        # set botvars so plugins can access when loading
        database.metadata = self.db_metadata
        database.base = self.db_base
        database.db = self.db
