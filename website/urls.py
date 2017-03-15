from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', views.user_login, name='user-login'),
]