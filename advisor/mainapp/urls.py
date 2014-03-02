from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from mainapp.views import * 
from mainapp.models import * 

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'coursegroups', CourseGroupViewSet)
router.register(r'trajectories', TrajectoryViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'buildresponses', BuildResponseViewSet)
router.register(r'requirements', RequirementViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^build/', build_trajectory, name='build-trac'),
    url(r'^new/', StartTrajectoryView.as_view(), name='new-trac'),
    #url(r'^search/', search, name='search'),
    #url(r'^student/(?P<slug>[^/]+)/$', DetailStudent.as_view(),
    #name='detail-student'),
    url(r'^profile/', profile, name='profile-detail'), 
    #name='profile'),
    url(r'^search/', include('haystack.urls')),
)

