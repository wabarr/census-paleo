from django.conf.urls import patterns, url
from login.views import user_login
urlpatterns = patterns('',
    url('',user_login, name="user_login"),


)


