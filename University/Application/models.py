from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django.shortcuts import render
from django.urls import reverse
from django.conf.urls import include, url


class Department(models.Model):
    dept_name = models.CharField(max_length=200, primary_key=True)
    building = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:department-detail', kwargs={'pk': self.pk})


class Student(models.Model):
    ID = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    tot_cred = models.IntegerField()
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:student-detail', kwargs={'pk': self.pk})

class Instructor(models.Model):
    ID = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:instructor-detail', kwargs={'pk': self.pk})

class Advisor(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True, default='10')
    i_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('Application:advisor-detail', kwargs={'pk': self.pk})

class Course(models.Model):
    course_id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=200)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:course-detail', kwargs={'pk': self.pk})

# class Prereq(models.Model):
#     num = models.IntegerField(default=10)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default='0')
#     # prereq_id = models.ForeignKey(Course, on_delete=models.CASCADE, default='1')

class Section(models.Model):
    def yearValidator(value):
        if (not(int(value) >= 2000 and int(value) <= int(datetime.datetime.now().year))):
            raise ValidationError(
                _('%(value) is not an valid year'),
                params={'value': value}
            )

    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_id = models.CharField(max_length=200)
    semester = models.IntegerField()
    year = models.IntegerField(validators=[yearValidator], default=2016)
    def get(self):
        return self.clean()
    def get_absolute_url(self):
        return reverse('Application:section-detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = (('course_id', 'sec_id', 'semester', 'year'),)



