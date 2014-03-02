from django.shortcuts import render, get_object_or_404, render_to_response 
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, ListView, DetailView, DeleteView,
UpdateView, FormView)

from rest_framework import viewsets
from braces.views import LoginRequiredMixin

from mainapp.serializers import (ProgramSerializer, CourseSerializer,
CourseGroupSerializer, TrajectorySerializer, SemesterSerializer,
BuildResponseSerializer, RequirementSerializer)
from mainapp.models import (Trajectory, Program, Major, Minor, GenEd,
Concentration, MetaCourse, Course, CourseGroup, Semester, BuildResponse,
Student, Requirement)
from mainapp.forms import StartTrajectoryForm, StudentForm
from mainapp.utils import genTrajectories
# Create your views here.
#FBV's
# Generic Views
@login_required
def build_trajectory(request):
    #process
    if request.method == "POST":
        form = StartTrajectoryForm(request.POST)
        #only lets you do one
        major = form['majors'].value() 
        minor = form['minors'].value()
        to_search_major = Major.objects.get(pk=major[0])
        to_search_minor = Minor.objects.get(pk=minor[0])
        programs = []
        programs.append(to_search_major)
        programs.append(to_search_minor)
        user_in = Student.objects.get(user__username=request.user.username)
        trac = genTrajectories(taken=None,programs=programs,user=user_in)
        #majors = form.fie
    return render_to_response('build.html', {
    })
class StartTrajectoryView(FormView):
    template_name = 'new.html'
    form_class = StartTrajectoryForm

# BEN MAKE THIS A CBV OR SOMETHING IDK
def search(request):
    return render_to_response('search.html', {
    })

#API SHIT
@login_required
def profile(request):
    current_user = get_object_or_404(Student,user__username=request.user.username)
    return render_to_response('profile.html', {
            "current_user" : current_user,
            "firstname" : current_user.user.first_name,
            "advisorname" : current_user.advisorname,
    })
class RequirementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupSerializer

class TrajectoryViewSet(viewsets.ModelViewSet):
    queryset = Trajectory.objects.all()
    serializer_class = TrajectorySerializer

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
class BuildResponseViewSet(viewsets.ModelViewSet):
    queryset = BuildResponse.objects.all()
    serializer_class = BuildResponseSerializer
#FORM CBV's

#Trajectory CBVS
class DetailBuildResponse(DetailView):
    model = BuildResponse
    template_name = 'build.html'

class CreateTrajectory(CreateView):
    model = Trajectory
#To Impement
'''
class ListTrajectory(ListView):
    pass
'''
class DetailTrajectory(DetailView):
    model = Trajectory

class DeleteTrajectory(DeleteView):
    model = Trajectory

class UpdateTrajectory(UpdateView):
    model = Trajectory

#Program CBVS
class CreateProgram(CreateView):
    model = Program

class ListProgram(ListView):
    model = Program

class DetailProgram(DetailView):
    model = Program

class DeleteProgram(DeleteView):
    model = Program

class UpdateProgram(UpdateView):
    model = Program

#Major CBVs
class ListMajor(ListView):
    model = Major

class DetailMajor(DetailView):
    model = Major

#Minor CBVs
class ListMinor(ListView):
    model = Minor

class DetailMinor(DetailView):
    model = Minor
#GenEd CBV
class ListGenEd(ListView):
    model = GenEd
class DetailGenEd(DetailView):
    model = GenEd
#Concentration CBV
class ListConcentration(ListView):
    model = Concentration

class DetailConcentration(DetailView):
    model = Concentration
#MetaCourse CBV
class ListMetaCourse(ListView):
    model = MetaCourse
class DetailMetaCourse(DetailView):
    model = MetaCourse
#Course CBV
class ListCourse(ListView):
    model = Course
class DetailCourse(DetailView):
    model = Course
#CourseGroup CBV
class ListCourseGroup(ListView):
    model = CourseGroup
class DetailCourseGroup(DetailView):
    model = CourseGroup
class DetailStudent(DetailView):
    model = Student
    template_name = 'student.html'

class CoursesTaken(UpdateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentForm
