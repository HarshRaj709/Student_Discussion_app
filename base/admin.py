from django.contrib import admin
from .models import Room,Topic,Message,UserProfile,Notification


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = [field.name for field in Room._meta.fields]

@admin.register(Topic)
class AdminTopic(admin.ModelAdmin):
    list_display = [field.name for field in Topic._meta.fields]

@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]

@admin.register(UserProfile)
class AdminProfile(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]

@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = [field.name for field in Notification._meta.fields]
