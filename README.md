# xonotic-cts-records

Parse the `server.db` from Xonotic into a SQLAlchemy, generate a highscore table.  Requires `sv_db_saveasdump 1` set in Xonotic defrag server.

## Install

Create a python3 venv and install `sqlalchemy`:

```
virtualenv -p /usr/bin/python3 venv
ln -s venv/bin/activate
source activate
pip install sqlalchemy
```

Copy your server.db file from your defrag server here:

```
cp ~/.xonotic/data/server.db .
```

## Usage


Run the parser:

```
python xrc.py
```

## License

GPLv3