from django.conf.urls import patterns, include, url
from upload.UploadCMS.views import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser, UserManager
from upload.UploadCMS.forms import UserCreationForm

from django.contrib import admin

urlpatterns = patterns(
    'upload.UploadCMS.views',
    url(r'^$', 'home', name='home'),
    url(r'^repositories/$', 'band_listing', name='repositories'),
    url(r'^repositories/(?P<pk>\d+)/$', 'band_detail', name='band_detail'),
    url(r'^bandform/$', BandForm.as_view(), name='band_form'),
    url(r'^memberform/$', MemberForm.as_view(), name='member_form'),
    url(r'^create_user/$',(CreateView.as_view(model=User, get_success_url =lambda: reverse_lazy('home'), form_class=UserCreationForm, template_name="bands/create_user.html")), name='create_user'),
    url(r'^login', 'login', name='login'),
    url(r'^contact/$', 'band_contact', name='contact'),
    url(r'^protected/$', 'protected_view', name='protected'),
    url(r'^accounts/login/$', 'message'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
