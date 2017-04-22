import configparser
import logging.config
import os

config_file = 'xcr.ini'
logging_config_file = 'xcr.logging.ini'

if not os.path.isfile(config_file):
    SystemExit('Config not found.')

config = configparser.ConfigParser()
config.read(config_file)

conf = {
    'database': config.get('xcr', 'database', fallback='sqlite:///xcr.db'),
}

logging.config.fileConfig(logging_config_file, defaults={
    'log_filename': os.path.expanduser('xcr.log')
})
