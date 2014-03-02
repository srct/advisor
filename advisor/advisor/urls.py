from django.conf.urls import patterns, include, url
from mainapp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('mainapp.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html'
        }),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': 'logout.html'})
)

