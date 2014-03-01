from django.conf.urls import patterns, include, url
from mainapp.views import (ProgramViewSet, CourseViewSet, CourseGroupViewSet,
    TrajectoryViewSet, build_trajectory)
#from .views import *
from mainapp.models import Program, Course, CourseGroup, Trajectory

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'coursegroups', CourseGroupViewSet)
router.register(r'trajectories', TrajectoryViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
)

