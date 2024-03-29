from django.shortcuts import render
from .models import Notification

def navbar_content(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')
    navbar_content = render(request, 'base/navbar.html', {'notifications': notifications}).content
    return {'navbar': navbar_content}
    # user = request.user
    # notifications = Notification.objects.filter(user = user)
    # return render(request,'base/navbar.html',{'notifications':notifications})

# not included in settings.py

