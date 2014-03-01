from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class Student(TimeStampedModel):
    user = models.OneToOneField(User)
    major = models.ForeignKey('Major')
    tj = models.OneToOneField('Trajectory')
    dateOfGrad = models.DateField()
    advisorname = models.OneToOneField('AdvisorAdminUser')
    coursestaken = models.ManyToManyField('Course')

    def __unicode__(self):
        return '%s' % self.user

class AdvisorAdminUser(TimeStampedModel):
    user = models.OneToOneField(User, related_name="advisorname")
    department = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.user


class Semester(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(Student)
    courses = models.ManyToManyField('Course')
    programs = models.ManyToManyField('Program')


class Trajectory(TimeStampedModel):
    user = models.OneToOneField(User, related_name="tj")
    semesters = models.ManyToManyField(Semester)
    completed = models.ManyToManyField('Course')


class Program(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True)
    courses = models.ManyToManyField('MetaCourse')

    def __unicode__(self):
        return '%s' % self.name


class Major(Program):
    gened = models.ForeignKey('GenEd')
    concentration = models.ForeignKey('Concentration', blank=True)


class Minor(Program):
    pass


class GenEd(Program):
    pass


class Concentration(Program):
    pass


class MetaCourse(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    catalogyear = models.IntegerField()
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.name


class Course(MetaCourse):
    dept = models.CharField(max_length=50)
    courseid = models.IntegerField()
    prerequisites = models.ManyToManyField(MetaCourse,
        blank=True, related_name='prereq+')
    corequisites = models.ManyToManyField(MetaCourse,
        blank=True, related_name='coreq+')
    credits = models.IntegerField()


class CourseGroup(MetaCourse):
    courses = models.ManyToManyField(Course)
    numneeded = models.IntegerField()
