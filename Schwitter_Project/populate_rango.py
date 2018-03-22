import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category,Page


def populate():
    



if __name__ == '__main__':
    print("starting Rango population script...")
    populate()
