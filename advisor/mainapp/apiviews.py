from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from rest_framework import viewsets
from .models import Trajectory, Program, Major, Minor, GenEd, Concentration,
MetaCourse, Course, CourseGroup
from .serializers import ProgramSerializer, CourseSerializer, CourseGroupSerializer, TrajectorySerializer

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

