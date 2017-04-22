import re
from xcr.session import Session


def main():
    xcr = Session()

    from xcr.models import MapRecord
    from xcr.models import Players

    with open('server.db.defrag') as f:
        for line in sorted(f):

            # time
            m = re.match('^\\\\([a-z0-9_-]+)/cts100record/time([0-9]+)\\\\([0-9]+)', line)
            if m:
                print(">>> {mapname} {rank} {time}".format(mapname=m.group(1), rank=m.group(2), time=m.group(3)))
                MapRecord.db_insert(mapname=m.group(1), rank=m.group(2), time=m.group(3))

            # uid2name
            m = re.match('^\\\\/uid2name/(.{40,})=\\\\(.+)', line)
            if m:
                print(">>> {uid} {player_name}".format(uid=m.group(1), player_name=m.group(2)))
                Players.db_insert(uid=m.group(1), player_name=m.group(2))


if __name__ == '__main__':
    main()
