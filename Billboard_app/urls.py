from django.conf.urls import url
from . import views
# from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    # url(r'^login$', login, name='login'),
    # url(r'^logout', logout, name='logout'),
    # url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^register$', views.register, name='register'),
    url(r'^home$', views.home, name='home'),
    url(r'^home/add_bb$', views.add_bb, name='Add New Billboard')
]