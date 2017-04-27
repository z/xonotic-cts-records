from sqlalchemy import desc, asc
from sqlalchemy.orm import eagerload
from sqlalchemy.sql import select

from xcr.model import MapRecordTime
from xcr.model import MapRecordSpeed
from xcr.model import Player
from xcr.model import PlayerToRecordTime
from xcr.model import PlayerToRecordSpeed

from xcr.util import database


class MapRecordTimeQuery:
    @staticmethod
    def db_insert(mapname, rank, time):
        new_map_record_time = MapRecordTime(
            mapname=mapname,
            rank=rank,
            time=time,
        )
        database.session.add(new_map_record_time)
        database.session.commit()

    # @staticmethod
    # def db_update(mapname, rank, time):
    #     query = map_record_time.update() \
    #         .where(map_record_time.c.mapname == mapname) \
    #         .values(rank=rank, time=time)
    #     database.session.execute(query)
    #     database.session.commit()

    @staticmethod
    def db_top_scores():

        # .join(player_to_record_time, map_record_time.mapname == player_to_record_time.mapname, map_record_time.rank == player_to_record_time.rank) \
        #.join(player_to_record_time.uid == player.uid) \
        # player_to_record_time, map_record_time.mapname == player_to_record_time.mapname, map_record_time.rank == player_to_record_time.rank)) \
        scores = database.session.query(MapRecordTime.mapname, MapRecordTime.rank, MapRecordTime.time) \
            .order_by(desc(MapRecordTime.mapname)) \
            .order_by(asc(MapRecordTime.rank))

        # scores = database.session.query(MapRecordTime).join(PlayerToRecordTime).join(Player)

        template = '_Top Scores_: '
        data = []

        for row in scores:
            template += '{} ({}): {:10.2f}\n'
            data.append(row.mapname)
            data.append(row.rank)
            data.append(row.time/100)
            #data.append(row.uid)

        template = template.rstrip(', ')
        if data:
            response = template.format(*data)
        else:
            response = "No scores here yet."

        return response


class MapRecordSpeedQuery:
    @staticmethod
    def db_insert(mapname, speed):
        new_map_record_speed = MapRecordSpeed(
            mapname=mapname,
            speed=speed,
        )
        database.session.add(new_map_record_speed)
        database.session.commit()


class PlayerQuery:
    @staticmethod
    def db_insert(uid, player_name):
        new_player = Player(
            uid=uid,
            player_name=player_name,
        )
        database.session.add(new_player)
        database.session.commit()


class PlayerToRecordTimeQuery:
    @staticmethod
    def db_insert(uid, rank, mapname):
        new_player_to_record_time = PlayerToRecordTime(
            uid=uid,
            rank=rank,
            mapname=mapname,
        )
        database.session.add(new_player_to_record_time)
        database.session.commit()


class PlayerToRecordSpeedQuery:
    @staticmethod
    def db_insert(uid, mapname):
        new_player_to_record_speed = PlayerToRecordSpeed(
            uid=uid,
            mapname=mapname,
        )
        database.session.add(new_player_to_record_speed)
        database.session.commit()
