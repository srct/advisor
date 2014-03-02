from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from mainapp.models import Student, Major, Minor, GenEd

# form on new page
class StartTrajectoryForm(forms.Form):
    majors = Major.objects.all()
    print majors
    minors = Minor.objects.all()
    print minors
    major = forms.ChoiceField(majors)
    minor = forms.ChoiceField(majors)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
'''
class SelectMajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ['name', ]
        exclude = ['slug', 'description', 'courses', 'gened', 'concentration',]
        labels = {
            'major' : 'Major',
        }
        widgets = {
            'major':forms.CharField(),
        }

class SelectMinorForm(forms.ModelForm):
    class Meta:
        model = Minor
        fields = ['name', ]
        exclude = ['slug', 'description', 'courses', ]
        labels = {
            'minor' : 'Minor',
        }
        widgets = {
            'minor':forms.CharField()
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
'''
