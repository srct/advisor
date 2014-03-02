from django.contrib import admin
from mainapp.models import *
# Register your Models here.


class StudentAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


class CourseGroupAdmin(admin.ModelAdmin):
    pass


class MajorAdmin(admin.ModelAdmin):
    pass


class MinorAdmin(admin.ModelAdmin):
    pass


class GenEdAdmin(admin.ModelAdmin):
    pass


class ConcentrationAdmin(admin.ModelAdmin):
    pass


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
