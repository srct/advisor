from django.conf.urls import patterns, include, url
import .apiviews
#from .views import *
from .models import Program, Course, CourseGroup, Trajectory

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', apiviews.ProgramViewSet)
router.register(r'courses', apiviews.CourseViewSet)
router.register(r'coursegroups', apiviews.CourseGroupViewSet)
router.register(r'trajectories', apiviews.TrajectoryViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
)

