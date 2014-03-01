from django.db import models

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    courses = models.ManyToManyField(MetaCourse)

    class Meta:
        abstract = True


class Major(Program):
    gened = models.ForeignKey(GenEd)
    concentration = models.ForeignKey(Concentration, blank=True)


class Minor(Program):
    pass


class GenEd(Program):
    pass


class Concentration(Program):
    pass


class MetaCourse(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    catalogyear = models.IntegerField()
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class Course(MetaCourse):
    prerequisites = models.ManyToManyField(MetaCourse)
    corequisites = models.ManyToManyField(MetaCourse, blank=True)


class CourseGroup(MetaCourse):
    courses = models.ManyToManyField(Course)
    numneeded = models.IntegerField()
