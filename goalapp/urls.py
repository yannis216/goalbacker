from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.front_site, name='front_site'),
]
