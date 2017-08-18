from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^city_centre/$', views.index_city_centre, name='index_city_centre' ),
    url(r'^new_college/$', views.index_new_college, name='index_new_college' ),
    url(r'^city_centre_results/$', views.city_centre_results, name='city_centre_results' ),
    url(r'^new_college_results/$', views.new_college_results, name='new_college_results' ),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail' ),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote' ),
]
