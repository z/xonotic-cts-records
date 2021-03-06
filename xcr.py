import re
import argparse

from xcr.session import Session


def main():
    xcr = Session()

    from xcr.resources import MapRecordTimeQuery
    from xcr.resources import MapRecordSpeedQuery
    from xcr.resources import PlayerQuery
    from xcr.resources import PlayerToRecordTimeQuery
    from xcr.resources import PlayerToRecordSpeedQuery

    # Setup args
    parser = argparse.ArgumentParser(description='Fun commanbs for xcr')

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    parser_parse = subparsers.add_parser('parse', help='parse maps into SQLite database')
    parser_records = subparsers.add_parser('records', help='print records')

    args = parser.parse_args()

    if args.command == 'records':
        print(MapRecordTimeQuery.db_top_scores())

    elif args.command == 'parse':

        with open('server.db.defrag') as f:
            for line in sorted(f):

                # time
                m = re.match('^\\\\([a-z0-9_-]+)/cts100record/time([0-9]+)\\\\([0-9]+)', line)
                if m:
                    print("[time] >>> {mapname} {rank} {time}".format(mapname=m.group(1), rank=m.group(2), time=m.group(3)))
                    MapRecordTimeQuery.db_insert(mapname=m.group(1), rank=m.group(2), time=m.group(3))

                # time to map
                m = re.match('^\\\\([a-z0-9_-]+)/cts100record/crypto_idfp([0-9]+)\\\\(.{40,})', line)
                if m:
                    print("[time to map] >>> {mapname} {uid}".format(mapname=m.group(1), rank=m.group(2), uid=m.group(3)))
                    PlayerToRecordTimeQuery.db_insert(mapname=m.group(1), rank=m.group(2), uid=m.group(3))

                # speed - qus
                m = re.match('^\\\\([a-z0-9_-]+)/cts100record/speed/speed\\\\([0-9]+(\.[0-9]+)?)', line)
                if m:
                    print("[speed] >>> {mapname} {speed}".format(mapname=m.group(1), speed=m.group(2)))
                    MapRecordSpeedQuery.db_insert(mapname=m.group(1), speed=m.group(2))

                # speed to map
                m = re.match('^\\\\([a-z0-9_-]+)/cts100record/speed/crypto_idfp\\\\(.{40,})', line)
                if m:
                    print("[speed to map] >>> {mapname} {uid}".format(mapname=m.group(1), uid=m.group(2)))
                    PlayerToRecordSpeedQuery.db_insert(mapname=m.group(1), uid=m.group(2))

                # uid2name
                m = re.match('^\\\\/uid2name/(.{40,})=\\\\(.+)', line)
                if m:
                    print("[uid2name] >>> {uid} {player_name}".format(uid=m.group(1), player_name=m.group(2)))
                    PlayerQuery.db_insert(uid=m.group(1), player_name=m.group(2))


if __name__ == '__main__':
    main()
