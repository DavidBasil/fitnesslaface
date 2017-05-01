from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from . import views


urlpatterns = [
    # login
    url(r'^login/$', login, name='login'),
    # logout
    url(r'^logout/$', logout, name='logout'),
    # logout then login
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    # user's dashboard
    url(r'^$', views.dashboard, name='dashboard'),
    # change password
    url(r'^password-change/$', password_change, name='password_change'),
    # change passord done
    url(r'^password-change/done/$', 
        password_change_done, 
        name='password_change_done'),
    # reset password
    url(r'^password-reset/$', password_reset, name='password_reset'),
    # reset password done
    url(r'^password-reset/done/$', 
        password_reset_done, 
        name='password_reset_done'),
    # reset password confirm
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm, name='password_reset_confirm'),
    # reset password complete
    url(r'^password-reset/complete/$', password_reset_complete,
        name='password_reset_complete'),
    # register new user
    url(r'^register/$', views.register, name='register'),
    # edit user/profile info
    url(r'^edit/$', views.edit, name='edit'),
]
