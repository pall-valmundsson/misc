from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^adagios/$', 'configurator.views.index'),
     (r'^adagios/configurator$', 'configurator.views.index'),
    (r'^adagios/configurator/host$', 'configurator.views.test'),
    (r'^adagios/configurator/host/(?P<host_name>.+)/(?P<service_description>.+)/(?P<field_name>.+)=(?P<new_value>.+)$', 'configurator.views.edit_service'),
    (r'^adagios/configurator/host/(?P<host_name>.+)/(?P<service_description>.+)$', 'configurator.views.service'),
    (r'^adagios/configurator/host/(?P<host_name>.+)$', 'configurator.views.host'),
    (r'^adagios/configurator/contact/(?P<contact_name>.+)$', 'configurator.views.contact'),
    (r'^adagios/configurator/contact$', 'configurator.views.list_contacts'),
    (r'^adagios/configurator/host/(?P<host_name>.+)/(?P<service_description>.+)$', 'configurator.views.service'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
