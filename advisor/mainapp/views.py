from django.shortcuts import render, get_object_or_404, render_to_response
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
# Create your views here.
#FBV's
# Generic Views
def build_trajectory(request):
    #process
    semester_key = 1
    return HttpResponse(semester_key)
def searchMajorMinor(request):
    #query
    if request.method == 'POST':
        form = StartTrajectoryForm(request.POST)
        if form.is_valid():
            #Queryset
            major = Major.objects.filter(name=form['major'])
            minor = Minor.objects.filter(name=form['minor'])
            #Check to seee if empty
            if major is None:
                msg = "Something Went Wrong"
            else:
                msg = "Found Object"
            return build_trajectory(request)

#API SHIT
@login_required
def profile(request):
    current_user = get_object_or_404(Student,user__username=request.user.username)

    return render_to_response('profile.html', {
            "user" : current_user,
    },
    context_instance = RequestContext(request),
    )

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
