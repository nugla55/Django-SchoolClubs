
from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('clubs/', views.all_clubs, name='clubs'),
    path('events/', views.all_events, name='events'),
    path('myclubs/<str:pk>', views.my_clubs, name='myclubs'),


    path('socialclubs/<str:pk>', views.socialclubs, name='socialclubs'),
    path('socialclubsdef/', views.socialclubs_def, name='socialclubs_def'),
    path('announcements/<str:pk>', views.announcement, name='announcement'),
    path('posts/<str:pk>', views.post, name='post'),
    path('chat/<str:pk>', views.chat, name='chat'),
    path('surveys/<str:pk>', views.survey, name='survey'),
    path('discussions/<str:pk>', views.discussion, name='discussion'),
    path('manage/', views.manage, name='manage'),
    path('manageclub/<str:pk>', views.manage_club, name='manage_club'),
    path('addClub/', views.addClub, name='addClub'),
    path('removeClub/<str:pk>', views.removeClub, name='removeClub'),

    path('message/', views.messages, name='message'),
    path('clubDetail/<str:pk>', views.clupDetail, name='clubDetail'),

    path('addpost<str:pk>/', views.addPost, name='addPost'),
    path('addevent<str:pk>/', views.addEvent, name='addEvent'),
    path('addsurvey/<str:pk>', views.addSurvey, name='addSurvey'),
    path('adddiscussion<str:pk>/', views.addDiscussion, name='addDiscussion'),
    path('join/<str:pk>', views.join, name='join'),
    path('leave/<str:pk>', views.leave, name='leave'),
    path('report/', views.report, name='report'),

    path('userpage/', views.userPage, name='userpage'),

    path('joinEvent/<str:pk>', views.joinEvent, name='joinEvent'),
    path('leaveEvent/<str:pk>', views.leaveEvent, name='leaveEvent'),
    path('eventpage<str:pk>/', views.eventPage, name='eventPage'),

    path('eventpagejoined/', views.eventPageJoined, name = 'eventPageJoined'),

    path('ccalendar/', views.ccalendar, name= 'ccalendar'),

]