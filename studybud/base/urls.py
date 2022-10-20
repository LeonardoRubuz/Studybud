from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),


    path('', views.home, name='home'),
    path('room/<int:id>', views.room, name='room'),
    path('profile/<int:id>', views.userProfile, name='userprofile'),

    path('create-room/', views.createRoom, name='createroom'),
    path('update-room/<int:id>', views.updateRoom, name='updateroom'),
    path('delete-room/<int:id>', views.deleteRoom, name='deleteroom'),
    path('delete-message/<int:id>', views.deleteMessage, name='deletemessage')

]