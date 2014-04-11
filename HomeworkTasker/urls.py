from django.conf.urls import patterns, include, url

from django.contrib import admin
import views
import formIns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HomeworkTasker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^register/',views.register),
    url(r'^loginInput/',formIns.loginForm),
    url(r'^registerInput/',formIns.registerForm),
    url(r'^addSubject/',formIns.addSubject),
    url(r'^addAssignment/',formIns.addAssignment),
    url(r'^removeAssignment/',formIns.removeAssignment), 
    url(r'^sortTasks/',formIns.sortTasks)   
)
