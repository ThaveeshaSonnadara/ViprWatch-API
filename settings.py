from os import environ

FLASK_DEBUG = environ.get('FLASK_DEBUG')
TF_ENABLE_ONEDNN_OPTS = environ.get('TF_ENABLE_ONEDNN_OPTS')
FLASK_RUN_PORT = environ.get('FLASK_RUN_PORT')
