import celery
from datetime import timedelta
from app import app
from phue import Bridge

@celery.task(name='toggleLightsTask')
def toggleLights():
    b = Bridge('192.168.1.103')
    b.connect()
    print b.lights