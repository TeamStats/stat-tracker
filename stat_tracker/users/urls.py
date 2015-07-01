from django.conf.urls import include, url
from users import views as user_views
from django.contrib.auth import views


urlpatterns = [
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^register/$', user_views.AddUserView.as_view(), name="user_register"),
    url(r'^logout/$', views.logout, {'next_page': 'login'}, name='logout'),
]
