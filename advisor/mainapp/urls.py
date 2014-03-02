from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from mainapp.views import (ProgramViewSet, CourseViewSet, CourseGroupViewSet,
TrajectoryViewSet, build_trajectory, SemesterViewSet, BuildResponseViewSet,
DetailStudent, ProfileView)
from mainapp.models import (Program, Course, CourseGroup, Trajectory, Semester,
BuildResponse, Student)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'coursegroups', CourseGroupViewSet)
router.register(r'trajectories', TrajectoryViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'buildresponses', BuildResponseViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', TemplateView.as_view(template_name='index.html')),
    url(r'^api', include(router.urls)),
    url(r'^build/', build_trajectory, name='build'),
    url(r'^student/(?P<slug>[^/]+)/$', DetailStudent.as_view(),
    name='detail-student'),
    url(r'^profile/(?P<slug>[^/]+)/$', ProfileView.as_view(), 
    name='profile'),
)

