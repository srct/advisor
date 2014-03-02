from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class Student(TimeStampedModel):
    user = models.OneToOneField(User)
    programs = models.ManyToManyField('Program')
    trajectory = models.OneToOneField('Trajectory', blank=True)
    dateOfGrad = models.DateField()
    advisorname = models.OneToOneField('AdvisorAdminUser', blank=True)

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
    courses = models.ManyToManyField('Course', blank=True)
    programs = models.ManyToManyField('Program')
    nextsemester = models.ForeignKey('self', blank=True, null=True)
    requirementssatisfied = models.ManyToManyField('Requirement',
        related_name="reqssatisfied+", blank=True)

    def __unicode__(self):
        return '%s' % self.number


class Trajectory(TimeStampedModel):
    user = models.OneToOneField(User, related_name="trajectory")
    semesters = models.ManyToManyField(Semester)


class Program(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True)
    requirements = models.ManyToManyField('Requirement',
        related_name="reqs+")

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


class Requirement(TimeStampedModel):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField('MetaCourse')


class MetaCourse(TimeStampedModel):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')
    catalogyear = models.IntegerField()
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.title


class Course(MetaCourse):
    uniqname = models.CharField(max_length=20,
        unique=True)
    dept = models.CharField(max_length=10)
    courseid = models.IntegerField()
    prerequisites = models.ManyToManyField(MetaCourse,
        blank=True, related_name='prereq+')
    corequisites = models.ManyToManyField(MetaCourse,
        blank=True, related_name='coreq+')
    credits = models.IntegerField()


class CourseGroup(MetaCourse):
    courses = models.ManyToManyField(Course)
    numneeded = models.IntegerField()
