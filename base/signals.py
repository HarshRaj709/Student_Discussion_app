# Import necessary modules
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import UserProfile

# Define signal receiver function to create UserProfile
@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):

    # Construct the profile picture path
    profile_pic_path = 'profile_pics/profile.png'  # Default profile picture path

    # # Check if the user signed up using Google or GitHub
    # if user.socialaccount_set.filter(provider='google'):
    #     profile_pic_path = 'profile_pics/google.jpg'  # Change profile picture path for Google
    # elif user.socialaccount_set.filter(provider='github'):
    #     profile_pic_path = 'profile_pics/profile.png'  # Change profile picture path for GitHub
        
    # Create UserProfile instance with default data and profile picture path
    UserProfile.objects.create(user=user, bio='Please Update your profile', profile_pic=profile_pic_path)
