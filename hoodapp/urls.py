from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/profile/(\d+)', views.profile, name='profile'),
    url(r'^new/edit_profile$', views.edit_profile, name='edit_profile'),
]