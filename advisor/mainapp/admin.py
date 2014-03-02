from django.contrib import admin
from django.contrib.auth.models import Group
from mainapp.models import *
# Register your Models here.


class StudentAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['dept', 'courseid']


class CourseGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']


class MajorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class MinorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class GenEdAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ConcentrationAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RequirementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseGroup, CourseGroupAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Minor, MinorAdmin)
admin.site.register(GenEd, GenEdAdmin)
admin.site.register(Concentration, ConcentrationAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.unregister(Group)
