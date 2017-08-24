import os
from datetime import timedelta
import celery

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

CELERY_BROKER_URL='redis://localhost:6379',
CELERY_RESULT_BACKEND='redis://localhost:6379'

CELERYBEAT_SCHEDULE = {
    'toggleLights': {
        'task': 'toggleLightsTask',
        'schedule': timedelta(seconds=5)
    },
}

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')