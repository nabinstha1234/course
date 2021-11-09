from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
import os

from django.db import connection


class Command(BaseCommand):
    help = 'Initial data'

    # sample usuage
    # ./manage.py state

    def handle(self, *args, **options):
        self._seed_state()

    def _seed_state(self):
        file_path = os.path.join(os.path.dirname(__file__), 'country.sql')
        sql_statement = open(file_path).read()
        with connection.cursor() as c:
            c.execute(sql_statement)



