from django.conf.urls import url, include
from datatrans import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
     # Example:
     # (r'^test_project/', include('test_project.foo.urls')),

     # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
     # to INSTALLED_APPS to enable admin documentation:
     # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

     # Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),
     url(r'^trans/', include(urls)),
]
