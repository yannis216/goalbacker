from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.front_site, name='front_site'),
    url(r'^add_info/(?P<pk>\d+)/$', views.add_info, name='add_info'),
    url(r'^user_goals/(?P<pk>\d+)/$', views.user_goals, name='user_goals'),
]
