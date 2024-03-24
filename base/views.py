from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from .models import Room,Topic,Message,UserProfile,Notification
from .forms import RoomForm,UserRegistration,UserForm,UserProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import os


def home(request):
    q = request.GET.get('q')    #we take this from 2 places 1: from side menu, other from search bar both have name=q
    if q:       #here we check for q
        # room = Room.objects.filter(topic__name__icontains=q)       #here we have to use double underscore to get parent value.

        #to handle more complex queries
        room = Room.objects.filter(Q(topic__name__icontains=q) |    #search through topic name
                                   Q(name__icontains = q ) |    #search through room name
                                   Q(description__icontains=q) |    #search through description
                                   Q(host__username__icontains = q))    #search through host's username, as host is foreign key, so we have to declare the field name from its parent.
    else:
        room = Room.objects.all()

    room_count=room.count()     #to get the count of rooms found which satisfies above queries.

    #lets create a query for Topic
    topics = Topic.objects.all()

    # Recent Activity Feature
    # recent_messages = Message.objects.all()#.order_by('-created','-updated')     #to get most recent messages
    if q:
        recent_messages = Message.objects.filter(Q(room__name__icontains=q))    #to show only those recent activity which are related to the room
    else:
        recent_messages = Message.objects.all()
    context = {'rooms':room,'topics':topics,'room_count':room_count,'recent_messages':recent_messages}
    return render(request,'base/home.html',context)

def room(request,pk):       
    room = Room.objects.get(id=pk)  #first we need to specify the target room then we can apply onetomany relation rule.
    messages1 = room.message_set.all().order_by('-created','-updated') #required _set.all() in 1 to many relations  #now show messages according to there created date  #here we are taking child of model name ='messages' and using _set.all() to get only those messages which belongs to our specified room.
    
    
    if request.method == 'POST':                            #mera logic working fine
        body = request.POST['message']                      #mera logic
        user = request.user                                     #mera logic
        saved = Message(user=user,room=room,body=body)      #mera logic

        words = body.split()
        tagged_usernames = [tag[1:] for tag in words if tag.startswith('@')]
        tagged_users = User.objects.filter(username__in = tagged_usernames)
        for tagged_user in tagged_users:
            notified = Notification.objects.create(user=tagged_user,tag_user=user.username,room=room,message=f'You have been tagged in a message by {user.username} in room {room.name}')
        # messages.success(request,'user tagged')
        # print(tagged_user)

        room.participants.add(user)                                     #yay working now whenever a new user write anything in the room he will get added into it.
        saved.save()                                        #mera logic
        return redirect('room',pk=room.id)  #agar ye nhi lgaya to reload krne pe messages khudse post hote rhenge

    #denis's logic 
    # if request.method == 'POST':
    #     message = Message.objects.create(
    #         user = request.user,
    #         room = room,
    #         body = request.POST.get('message')
    #     )
    #     return redirect('room',pk=room.id)      #we will land on same page bydefault,not necessary but it will help to handle functionality more acurately
        
    #handle participants
    particpants = room.participants.all()       #to get all participants as it is manytomany field we access it by all() simply rather than _set.all()
    parti_count = particpants.count()       # count them

    #Problem user not joined from themselve -----solved line 41
    
    room_user = room.host
    context = {'notification':Notification,'room_user':room_user,'room':room,'room_messages':messages1,'participants':particpants,'count':parti_count}
    return render(request,'base/room.html',context)



@login_required(login_url='loginhandler')
def createRoom(request):
    host = request.user     #take the loggedin user
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST['topic']  #take input from topic
        room_name = request.POST['name']
        if room_name == '':
            messages.error(request,'Please enter room name')
            return redirect('createroom')
        description = request.POST['description']
        # topic,created = Topic.objects.get_or_create(name=topic_name)   #topic, created = ...: This line unpacks the tuple returned by get_or_create() into two variables, topic and created. topic will contain the retrieved or newly created Topic object, and created will be a boolean indicating whether the object was newly created (True) or retrieved from the database (False)
        topic = Topic.objects.filter(name__iexact=topic_name).first()       #now no one can create 2 topic of ame name by using 1st letter capital in one and small in other.
        if not topic:
            topic = Topic.objects.create(name=topic_name)
        
        #my method
        # fm = RoomForm(request.POST)
        # if fm.is_valid():
        #     topic_name = fm.cleaned_data['topic']
        #     topic,created = Topic.objects.get_or_create(name=topic_name)
        #     name = fm.cleaned_data['name']
        #     description = fm.cleaned_data['description']
        #     room_save = Room(
        #         host = host,
        #         topic = topic,
        #         name = name,
        #         description = description,
        #     )
        #     room_save.save()

        # dennis Ivy method

        Room.objects.create(
            host = host,
            topic = topic,
            name = room_name,
            description = description,
        )

           
        #     room = fm.save(commit=False)#we want that only the room is created by the logedin user so thats why here we
        #             #we created a room object to get all the details from the form but place loggedin user as host.
        #     room.host = host    #here we place that
        #     room.save()         #now save that room

            # fm.save()     here we directly save the data which all user to choose amoung all user as host. And removed host option from form by using 'excude'

        return redirect('home')
        # else:
        #     print(fm.errors)
        #     messages.error(request,'inavlid Entry')
        #     return redirect('createroom')
    else:
        fm = RoomForm()
    return render(request,'base/room_form.html',{'form':fm,'topics':topics})


@login_required(login_url='loginhandler')
def updateRoom(request,pk):     #5:09:58
    room = Room.objects.get(pk=pk)          #from here we are getting the form data as we used {{room.name}} in our form.
    topics = Topic.objects.all()
    if request.user != room.host:       #only user who created room will be able to delete room
        return HttpResponse('you are not allowed to Edit others Room.')
    

    if request.method == 'POST':
        # ab isko new data se save krne ke liye ye kiya h. main h iski html template jisme automatically data le rhe h.
        topic_name = request.POST['topic']  #take input from topic
        topic,created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST['name']
        room.topic = topic
        room.description = request.POST['description']
        room.save()
        # print('saved')
        return redirect('home')
        # fm = RoomForm(request.POST,instance=room)
        # if fm.is_valid():
        #     fm.save()
        #     return redirect('home')
        # else:
        #     messages.success(request,'inavlid Entry')
        #     return redirect('createroom')
    # else:
    #     fm = RoomForm(instance=room)
    return render(request,'base/room_update.html',{'topics':topics,'room':room})
    


@login_required(login_url='loginhandler')
def deleteRoom(request,pk):
    delete = Room.objects.get(pk=pk)
    topic = delete.topic
    room_count = delete.topic.room_set.all().count()        #this will work also
    # room_count = Room.objects.filter(topic=topic).count()     #this will also work,easy to understand approach
    # print(room_count)
    if request.user != delete.host:     #only user who created room will be able to delete room
        return HttpResponse('you are not allowed to Delete others Room.')
    if request.method == 'POST':      #Easisest way to delete but we will render an html file which will ask user he rally want to delete or not.
        delete.delete()
        # print('room deleted')
        if room_count <= 1:
            topic.delete()
            # print('deleted')
        # else:
        #     print('greater then 1')
        return redirect('home')
    return render(request,'base/delete.html',{'delete':delete})


#Register user

def register_user(request):
    if not request.user.is_authenticated:
        page = 'register'       #gazab maza agya, same page will work for both 'login/register'
        if request.method == 'POST':
            fm = UserRegistration(request.POST) 
            if fm.is_valid():
                f_name = fm.cleaned_data['firstName']
                l_name = fm.cleaned_data['lastName']
                email = fm.cleaned_data['email']
                password = fm.cleaned_data['password']
                username = fm.cleaned_data['username']
                user = User(first_name=f_name,last_name=l_name,email=email,username=username)
                user.set_password(password)
                user.save()
                # Saving default Data in users profile. so that not get error while trying to see new users profile.NOw i created signals so no need to specify here.
                profile_pic_path = os.path.join('profile_pics', 'profile.png')
                profile = UserProfile.objects.create(user=user,bio='Update your Profile',profile_pic=profile_pic_path)
                person = authenticate(username=username,password=password)
                if person is not None:
                    login(request,person)
                    return redirect('home')
            else:
                # messages.error(request,'Please enter correct details')
                return render(request,'base/login_register.html',{'page':page,'form':fm})
        else:
            fm = UserRegistration()
        return render(request,'base/login_register.html',{'page':page,'form':fm})
    else:
        return redirect('home')



#Handle login/registration work here

def login_user(request):
    page = 'login'       #gazab maza agya, same page will work for both 'login/register'
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'User login successful')
                return redirect('home')
            else:
                messages.error(request,'wrong credentials')
        return render(request,'base/login_register.html',{'page':page})
    else:
        return redirect('home')

@login_required(login_url='loginhandler')
def user_profile(request,id):
    q = request.GET.get('q')
    user = User.objects.get(pk=id)
    profile = UserProfile.objects.get(user=user)
    room = user.room_set.all()      #as we are accessing in reverse oreder according to our model we write 'room' not 'Room' and '_set' to access its element.
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    room_count = rooms.count()
    recent_messages = user.message_set.all()        #to get only those messages who relates to 1 user.

    context = {'profile':profile,'user':user,'rooms':room,'room1':rooms,'room_count':room_count,'topics':topics,'recent_messages':recent_messages}
    return render(request,'base/profile.html',context)




@login_required(login_url='loginhandler')
def update_pro(request,id):             #here i used pk method but denis Ivy used request.user method to identify user.
    user = User.objects.get(pk=id)
    profile = UserProfile.objects.get(user=user)        #used this to get users profile bio
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, 'User info and profile updated Successfully')
            return redirect(reverse('profile', args=[user.id]))  #this is how you can handle dynamic urls through redirect method
            # return render(request,'base/profile.html',{'user':user}) this will also work but not good for my project 
        else:
            return render(request, 'base/Profile_update.html', {'user': user, 'user_form': user_form,'profile':profile,'profile_form':profile_form})
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user)
    return render(request, 'base/Profile_update.html', {'user': user, 'user_form': user_form,'profile':profile})



def logout_user(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('home')



# Handling messages deletion 

@login_required(login_url='loginhandler')
def deletemessage(request,pk):
    page = 'message'
    message = Message.objects.get(pk=pk)

    if request.user != message.user:     #only user who created room will be able to delete room
        return HttpResponse('you are not allowed to Delete others Room.')
    
    if request.method == 'POST':      #Easisest way to delete but we will render an html file which will ask user he rally want to delete or not.
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'delete':message,'page':page})


def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user = user).order_by('-timestamp')
    for notification in notifications:
        notification.boolean = True
        notification.save()
    context = {'notification':notifications}
    return render(request,'base/notification.html',context)

