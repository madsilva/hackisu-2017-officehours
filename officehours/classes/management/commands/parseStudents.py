import csv
import sys

from django.core.management.base import BaseCommand

from classes.models import Student, Course

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('stud_file', type=str)

    def handle(self, *args, **options):
        course=Course.objects.get(name='hackISU')
        #course=Course.objects.create(name='hackISU', year='2017', semester='FA', course_number='0001')
        #course.save()
        with open(options['stud_file'], 'r') as stud_file:
            stud_file.readline()
            stud_reader = csv.reader(stud_file)
            for row in stud_reader:
                stud_info = row
                student = Student.objects.create(full_name=stud_info[0], canvas_id=stud_info[1], section=stud_info[2], course=course)
                student.save()
