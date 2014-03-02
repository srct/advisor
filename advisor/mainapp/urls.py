from django.conf.urls import patterns, include, url
from mainapp.views import (ProgramViewSet, CourseViewSet, CourseGroupViewSet,
    TrajectoryViewSet, build_trajectory, SemesterViewSet)
from mainapp.models import Program, Course, CourseGroup, Trajectory, Semester

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'coursegroups', CourseGroupViewSet)
router.register(r'trajectories', TrajectoryViewSet)
router.register(r'semesters', SemesterViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^build/', build_trajectory, name='build')
)

