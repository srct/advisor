from django.conf.urls import patterns, include, url
from mainapp import views
#from .views import *
from mainapp.models import Program, Course, CourseGroup, Trajectory

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', views.ProgramViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'coursegroups', views.CourseGroupViewSet)
router.register(r'trajectories', views.TrajectoryViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
)

