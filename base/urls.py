from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #room related
    path('room/<int:pk>/',views.room,name='room'),
    path('room_create/',views.createRoom,name='createroom'),
    path('room_update/<int:pk>/',views.updateRoom,name='updateroom'),
    path('room_delete/<int:pk>/',views.deleteRoom,name='deleteroom'),
    #user register related
    path('login/',views.login_user,name='loginhandler'),
    path('Register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logouthandler'),
    path('profile/<int:id>',views.user_profile,name='profile'),
    path('profile_update/<int:id>',views.update_pro,name='profile_up'),
    #message related
    path('message-delete/<int:pk>/',views.deletemessage,name='message-delete'),
    #notification related
    path('Notifications/',views.notifications,name='notify')
]
