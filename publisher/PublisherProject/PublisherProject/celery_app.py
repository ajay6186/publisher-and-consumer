from celery import Celery

# Create a Celery instance
celery_app = Celery('myapp', broker='pyamqp://guest:guest@localhost//')

# Define a simple task
@celery_app.task
def add(x, y):
    return x + y
