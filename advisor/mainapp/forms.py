from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from mainapp.models import Student, Major, Minor, GenEd

# form on new page
class NewMajorForm( ModelForm ):
    class Meta:
        model = Major
        fields = [
        ]
        exclude = [
        ]
        labels = {
        }
        widgets = {
        }

# form on build page
class BuildSemesterForm( ModelForm ):
    class Meta:
        model = Semester
        fields = [
        ]
        exclude = [
        ]
        labels = {
        }
        widgets = {
        }

# form on user page
class StudentUpdateForm( ModelForm ):
    class Meta:
        model = Student
        fields = [
        ]
        exclude = (
        )
        labels = {
        }
        widgets = {
        }
