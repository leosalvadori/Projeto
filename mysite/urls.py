from django.conf.urls import patterns, include, url
from mysite.UploadCMS.views import *

from django.contrib import admin

urlpatterns = patterns(
    'mysite.UploadCMS.views',
    url(r'^$', 'home', name='home'),
    url(r'^repositorios/$', 'band_listing', name='Repositorio'),
    url(r'^repositorios/(?P<pk>\d+)/$', 'band_detail', name='band_detail'),
    url(r'^bandform/$', BandForm.as_view(), name='band_form'),
    url(r'^memberform/$', MemberForm.as_view(), name='member_form'),
    url(r'^contact/$', 'band_contact', name='contact'),
    url(r'^protected/$', 'protected_view', name='protected'),
    url(r'^accounts/login/$', 'message'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
