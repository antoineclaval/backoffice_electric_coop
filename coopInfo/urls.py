from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from coopInfo import views

urlpatterns = [
    url(r'^persons/$', views.PersonList.as_view()),
    url(r'^persons/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)