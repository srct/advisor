from django.contrib import admin
from django.contrib.auth.models import Group
from mainapp.models import *
# Register your Models here.


class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('programs', 'coursestaken',)


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['dept', 'courseid']
    filter_horizontal = ('prerequisites', 'corequisites',)


class CourseGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ('courses',)


class MajorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ('requirements', 'concentrations',)


class MinorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ('requirements',)


class GenEdAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ('requirements',)


class ConcentrationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ('requirements',)


class RequirementAdmin(admin.ModelAdmin):
    filter_horizontal = ('courses',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseGroup, CourseGroupAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Minor, MinorAdmin)
admin.site.register(GenEd, GenEdAdmin)
admin.site.register(Concentration, ConcentrationAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.unregister(Group)
