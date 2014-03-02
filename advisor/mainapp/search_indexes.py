from haystack import indexes
from django.utils import timezone # reqired for when the indexes were last updated
from mainapp.models import Course, Major, Minor

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField( document = True, use_template = True)

    #title = indexes.CharField( model_attr = "title" )
    catalogyear = indexes.CharField( model_attr = "catalogyear" )
    #description = indexes.CharField( model_attr = "description" )
    #dept = indexes.CharField( model_attr = "dept" )
    #courseid = indexes.CharField( model_attr = "courseid" )
    credits = indexes.CharField( model_attr = "credits" )

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class MajorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template = True)

    #name = indexes.CharField(model_attr = "name")
    #description = indexes.CharField(model_attr = "description")

    def get_model(self):
        return Major

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class MinorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template = True)

    #name = indexes.CharField(model_attr = "name")
    #description = indexes.CharField(model_attr = "description")

    def get_model(self):
        return Minor

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
