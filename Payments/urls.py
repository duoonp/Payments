from django.conf.urls import patterns, include, url
from Payments.views import * #EmployeeAddForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page),
# Session managment
    url(r'^logout/$', logout_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
# Admin page
    url(r'^admin/', include(admin.site.urls)),
	url(r'^employees/add/$', employee_add),

 #   url(r'^employees/add/$', EmployeeAddFormView.as_view()),
)
