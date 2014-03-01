from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from rest_framework import viewsets

from mainapp.serializers import ProgramSerializer, CourseSerializer, CourseGroupSerializer, TrajectorySerializer
from mainapp.models import Trajectory, Program, Major, Minor, GenEd, Concentration, MetaCourse, Course, CourseGroup
# Create your views here.
#API SHIT

class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class CourseSerializer(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseGroupSerializer(viewsets.ReadOnlyModelViewSet):
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupSerializer


class TrajectorySerializer(viewsets.ModelViewSet):
    queryset = Trajectory.objects.all()
    serializer_class = TrajectorySerializer

#Trajectory CBVS
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
