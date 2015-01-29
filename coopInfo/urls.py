from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from coopInfo import views

urlpatterns = [
    url(r'^persons/$', views.PersonList.as_view()),
    url(r'^persons/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),
    url(r'^states/$', views.StateList.as_view()),
    url(r'^states/(?P<pk>[0-9]+)/$', views.StateDetail.as_view()),
    url(r'^cooperatives/$', views.CooperativeList.as_view()),
    url(r'^cooperatives/(?P<pk>[0-9]+)/$', views.CooperativeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)