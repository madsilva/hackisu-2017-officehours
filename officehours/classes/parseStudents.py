import csv
import sys
from . import views

path = sys.argv[1]

with open(path) as stud_file:
    stud_file.readline()
    stud_reader = csv.reader(stud_file)
    for row in stud_reader:
        stud_info = row.split(',')
        student = Student.objects.create(full_name=stud_info[0], hawkid=stud_info[1], section=stud_info[2])


