from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class9_10_ssc/', views.class9_10_SSC, name='class9_10_ssc'),
    path('contactus/', views.contactUs, name='contactus'),
    path('enrollnow/', views.enrollNow, name='enrollnow'),
    path('highereducation_studyabroad/', views.higherEducation_studyAbroad, name='highereducation_studyabroad'),
    path('onlineschool/', views.onlineSchool, name='onlineschool'),
    path('policiesprocedures/', views.policiesProcedures, name='policiesprocedures'),
    path('skillbasedECprograms/', views.skillBasedECPrograms, name='skillbasedECprograms'),
    path('whychoosesl/', views.whyChooseSL, name='whychoosesl'),
    path('free-education/', views.free_education_view, name='free_education'),
]
