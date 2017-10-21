from django.db import models


class Course(models.Model):
    """
    Docstring goes here theoretically
    """

    semester_choices = (('FA', 'Fall'),
                        ('SP', 'Spring'),
                        ('WI', 'Winter'),
                        ('SU', 'Summer'))

    # name of course ie "Engineering Problem Solving II"
    name = models.CharField(max_length=200)
    # course number ie CS2820
    course_number = models.CharField(max_length=10)
    semester = models.CharField(choices=semester_choices)
    year = models.TextField(max_length=4)

    class Meta:
        unique_together = ['year', 'semester', 'course_number']


class Student(models.Model):
    """
    Docstring goes here theoretically
    """

    hawkid = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    course = models.ForeignKey(model=Course, on_delete=models.CASCADE)
    times_signed_in_to_session = models.IntegerField(default=0)
    current_session = models.ForeignKey(model=Session, blank=True, null=True, default=None)


class Session(models.Model):
    """
    Docstring goes here theoretically
    """

    course = models.ForeignKey(model=Course, on_delete=models.CASCADE)
    date = models.DateField()



class Question(models.Model):
    text = models.TextField()
    student = models.ForeignKey(model=Student, on_delete=models.CASCADE)
    session = models.ForeignKey(model=Session, on_delete=models.CASCADE)