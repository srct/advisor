from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from mainapp.models import Student, Major, Minor, GenEd

# form on new page
class NewMajorForm( ModelForm ):
    class Meta:
        model = Major
        fields = ['name',
        # not immediately sure how to take other objects as fields
        # 'concentration',
        ]
        exclude = ['slug', 'description', 'courses', 'gened',
        # remove when figure out how
        'concentration',
        ]
        labels = {
        'name':'Major',
        # 'concentration':'Concentration',
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Government and International Politics',
            }),
            # 'concentration':forms.TextInput(attrs={
            #    'name':
        }

class NewMinorForm( ModelForm ):
        model = Semester
        fields = ['name', ]
        exclude = ['slug', 'description', 'courses', ]
        labels = {
            'name':'Minor',
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Software Engineering',
            }),
        }

# form on build page
class BuildSemesterForm( ModelForm ):
    class Meta:
        model = Semester
        fields = ['courses', ]
        exclude = ['number', 'user', ]
        labels = {
            'courses' : 'Possible Courses',
        }
        widgets = {
            'courses':forms.CheckboxSelectMultiple(attrs={
                'class':'form-control',
                'placeholder':'',
            }),
        }

# form on user page
class StudentUpdateForm( ModelForm ):
    class Meta:
        model = Student
        fields = [ ]
        exclude = (
        )
        labels = {
        }
        widgets = {
        }
