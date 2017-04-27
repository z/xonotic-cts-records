from sqlalchemy import Table, Column, String, Integer, Float
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, backref

from xcr.util import database


uid2name = Table('uid2player', database.metadata,
    Column('uid', Integer, ForeignKey('player_to_record_time.uid')),
    Column('player_uid', Integer, ForeignKey('player.uid')),
)


class MapRecordTime(database.base):
    __tablename__ = 'map_record_time'
    id = Column(Integer, primary_key=True)
    mapname = Column(String(120))
    rank = Column(Integer)
    time = Column(Integer)
    PrimaryKeyConstraint('mapname', 'rank')

    # player = relationship(PlayerToRecordTime, primaryjoin=rank == PlayerToRecordTime.rank, secondaryjoin=mapname == PlayerToRecordTime.mapname, backref='player_to_record_time')


class MapRecordSpeed(database.base):
    __tablename__ = 'map_record_speed'
    id = Column(Integer, primary_key=True)
    mapname = Column(String(120))
    speed = Column(Float)


class Player(database.base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    uid = Column(String(60))
    player_name = Column(String(120))


class PlayerToRecordTime(database.base):
    __tablename__ = "player_to_record_time"
    id = Column(Integer, primary_key=True)
    uid = Column(String(60))
    rank = Column(Integer)
    mapname = Column(String(120))
    PrimaryKeyConstraint('mapname', 'rank')


class PlayerToRecordSpeed(database.base):
    id = Column(Integer, primary_key=True)
    __tablename__ = "player_to_record_speed"
    uid = Column(String(60))
    mapname = Column(String(120))


database.metadata.create_all()
