from django.db import models


class Course(models.Model):
    """
    Docstring goes here theoretically
    """

    # name of course ie "Engineering Problem Solving II"
    name = models.CharField(max_length=200)
    # course number ie CS2820
    course_number = models.CharField(max_length=10)


class Student(models.Model):
    """
    Docstring goes here theoretically
    """

    hawkid = models.CharField(max_length=20)
    full_name = models.CharField(max_length=150)

    course = models.ForeignKey(model=Course, on_delete=models.CASCADE())


class Session(models.Model):


    course = models.ForeignKey(model=Course, on_delete=models.CASCADE())
    # how to associate TAs?


class Question(models.Model):
    text = models.TextField()
    student = models.ForeignKey(model=Student, on_delete=models.CASCADE())