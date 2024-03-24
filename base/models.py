from django.db import models
from django.contrib.auth.models import User

#Everything related to topic
class Topic(models.Model):      
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



#everything related with Room
class Room(models.Model):   
    host = models.ForeignKey(User,on_delete = models.SET_NULL,null = True) #1tomany relation so to access this via User we use '_set'
    topic = models.ForeignKey(Topic,on_delete = models.SET_NULL,null = True) #if any specific topic get delete then all rooms made on that topic not get deleted. and we set models.SET_NULL then we have to null = True which allow db to store null values.
    name = models.CharField(max_length=100)
    description = models.TextField(null = True,blank = True) #This field allows for large amounts of text and can be left empty (null=True) or blank (blank=True) if not provided. This is useful if the description is optional.
    participants = models.ManyToManyField(User,related_name='participants',blank=True) #'related_name=' i used it here because as we can see we already have a relationship with User model in host field so to again use same model but with different relationship we need to specifies it's 'related_name'
    updated = models.DateTimeField(auto_now = True) #Every time we update a room, this value will get updated.
    created = models.DateTimeField(auto_now_add = True) #update only for 1 time

    class Meta:
        ordering = ['-updated','-created']      #showing newest updated item first

    def __str__(self):
        return self.name




#everything realated with messages
class Message(models.Model):    
    user = models.ForeignKey(User,on_delete=models.CASCADE) #1 to many relationship as 1 user can send multiple messaegs.
    room = models.ForeignKey(Room,on_delete=models.CASCADE) #here model message have 1 to many relationship with room model,means 1 room have multiple messages and i used models.CASCADE because when room get deleted all its message also get deleted.
    body = models.TextField()   #actual messsage
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created','-updated']

    # def __str__(self):
    #     return self.body[0:50]        # not working in my case i dont know why
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True, null=True)

    def __str__(self):
        return self.user.username
    


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    tag_user = models.CharField(max_length=100)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    boolean = models.BooleanField(default = False)