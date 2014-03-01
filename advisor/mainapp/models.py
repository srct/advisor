from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AdvisorUser(TimeStampedModel):
    user = models.OneToOneField(User)
    tj = models.ForeignKey(Trajectory)

    def __unicode__(self):
        return '%s' % self.user

class Trajectory(TimeStampedModel):
    pass

class Program(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True)
    courses = models.ManyToManyField(MetaCourse)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s' % self.name


class Major(Program):
    gened = models.ForeignKey(GenEd)
    concentration = models.ForeignKey(Concentration, blank=True)


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

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s' % self.name


class Course(MetaCourse):
    prerequisites = models.ManyToManyField(MetaCourse)
    corequisites = models.ManyToManyField(MetaCourse, blank=True)


class CourseGroup(MetaCourse):
    courses = models.ManyToManyField(Course)
    numneeded = models.IntegerField()
