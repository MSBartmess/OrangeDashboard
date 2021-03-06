from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

celery.add_periodic_task

from app import views, models, tasks