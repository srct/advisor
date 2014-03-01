from django.conf.urls import patterns, include, url
import apiviews
from .views import *
from .models import Program, Course, CourseGroup, Trajectory

from rest_framework.routers import DefaultRouter

'''
program_list = ProgramViewSet.as_view({
    'get' : 'list'
})

program_detail = ProgramViewSet.as_view({
    'get' : 'retrieve',
})

course_list = CourseViewSet.as_view({
    'get': 'list'
})

course_detail = ProgramViewSet.as_view({
    'get' : 'retrieve'
})

coursegroup_list = CourseGroupViewSet.as_view({
    'get' : 'list'
})

coursegroup_detail = CourseGroupViewSet.as_view({
    'get' : 'retreive'
})

trajectory_list = TrajectoryViewSet.as_view({
    'post' : 'create'
})

trajectory_detail = TrajectoryViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})
'''
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
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    '''
    url(r'^advisor/program/$' program_list, name='program-list'),
    url(r'^advisor/program/(?<pk>[0-9]+)/$', program_detail,
    name='program-detail'),
    url(r'^advisor/course/$', course_list, name='course-list'),
    url(r'^advisor/course/(?<pk>[0-9]+)/$', course_detail,
    name='course-detail'),
    url(r'advisor/coursegroup/$', coursegroup_list, name='coursegroup-list'),
    url(r'^advisor/coursegroup/(?<pk>[0-9]+)/$', coursegroup_detail,
    name='coursegroup-detail')
    url(r'advisor/trajectory/$', trajectory_list, name='trajectory-list'),
    url(r'advisor/trajectory/(?<pk>[0-9]+)/$', trajectory_detail,
    name='trajectory-detail'),
    '''
)

