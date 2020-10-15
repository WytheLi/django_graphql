from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('beatserver/', views.beatserver, name='beatserver'),
    path('<str:room_name>/', views.room, name='room'),
]