# -*- coding: utf-8 -*-

"""Main module."""

import logging
import yaml
import sys
import os

from flask import Flask


app = Flask(__name__)
logger = logging.getLogger()

DEBUG = bool(os.environ.get('DEBUG', False))
if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

CONFIG_PATH = os.environ.get('CONFIG_PATH', 'config.yml')
_config = None


def load_config(config_path):
    if not _config:
        try:
            with open(config_path) as f:
                _config = yaml.load(f.read())
        except IOError as ioerr:
            logger.error('load_config: unable to read config file. did you set ' +
                         'CONFIG_PATH correctly? error received: {}'.format(ioerr.strerror))
            sys.exit(-1)
    return _config

@app.route('/')
def helloworld():
    logger.debug('helloworld: yay! the app started!')

    # plan to add config override param to app for dev/test.
    # for now, we use the defaulr or whatever is passed in at startup.
    config = load_config(CONFIG_PATH)
    return 'Moo!'
