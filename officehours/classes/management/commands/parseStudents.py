import csv
import sys

from django.core.management.base import BaseCommand

from classes.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('stud_file', type=str)

    def handle(self, *args, **options):
        with open(options['stud_file']) as stud_file:
            stud_file.readline()
            stud_reader = csv.reader(stud_file)
            for row in stud_reader:
                stud_info = row.split(',')
                student = Student.objects.create(full_name=stud_info[0], hawkid=stud_info[1], section=stud_info[2])
                student.save()