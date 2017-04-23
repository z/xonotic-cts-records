from sqlalchemy import Table, Column, String, Integer, Float, PrimaryKeyConstraint, desc
from sqlalchemy.sql import select

from xcr.util import database

table_map_record_time = Table(
    "map_record_time",
    database.metadata,
    Column("mapname", String(120)),
    Column("rank", Integer),
    Column("time", Integer),
    PrimaryKeyConstraint('mapname', 'rank'),
)

table_map_record_speed = Table(
    "map_record_speed",
    database.metadata,
    Column("mapname", String(120)),
    Column("speed", Float),
)

table_player = Table(
    "player",
    database.metadata,
    Column("uid", String(60)),
    Column("player_name", String(120)),
)

table_player_to_record_time = Table(
    "player_to_record_time",
    database.metadata,
    Column("uid", String(60)),
    Column("mapname", String(120)),
)

table_player_to_record_speed = Table(
    "player_to_record_speed",
    database.metadata,
    Column("uid", String(60)),
    Column("mapname", String(120)),
)

database.metadata.create_all()


class MapRecordTime:
    @staticmethod
    def db_insert(mapname, rank, time):
        query = table_map_record_time.insert().values(
            mapname=mapname,
            rank=rank,
            time=time,
        )
        database.db.execute(query)
        database.db.commit()

    @staticmethod
    def db_update(mapname, rank, time):
        query = table_map_record_time.update() \
            .where(table_map_record_time.c.mapname == mapname) \
            .values(rank=rank, time=time)
        database.db.execute(query)
        database.db.commit()

    @staticmethod
    def db_top_scores():
        query = select([table_map_record_time.c.mapname, table_map_record_time.c.rank, table_map_record_time.c.time]) \
                       .order_by(desc(table_map_record_time.c.mapname)) \
                       .order_by(desc(table_map_record_time.c.rank))
        scores = database.db.execute(query)

        template = '_Top Scores_: '
        data = []

        for row in scores:
            template += '*{}*: {}, '
            data.append(row.name)
            data.append(row.score)

        template = template.rstrip(', ')
        if data:
            response = template.format(*data)
        else:
            response = "No scores here yet."

        return response


class MapRecordSpeed:
    @staticmethod
    def db_insert(mapname, speed):
        query = table_map_record_speed.insert().values(
            mapname=mapname,
            speed=speed,
        )
        database.db.execute(query)
        database.db.commit()


class Player:
    @staticmethod
    def db_insert(uid, player_name):
        query = table_player.insert().values(
            uid=uid,
            player_name=player_name,
        )
        database.db.execute(query)
        database.db.commit()


class PlayerToMapRecordTime:
    @staticmethod
    def db_insert(uid, mapname):
        query = table_player_to_record_time.insert().values(
            uid=uid,
            mapname=mapname,
        )
        database.db.execute(query)
        database.db.commit()


class PlayerToMapRecordSpeed:
    @staticmethod
    def db_insert(uid, mapname):
        query = table_player_to_record_speed.insert().values(
            uid=uid,
            mapname=mapname,
        )
        database.db.execute(query)
        database.db.commit()
