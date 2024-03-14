from django import forms
from .models import Room,UserProfile
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        # fields = '__all__'  #for now take all the fields of model Room.
        exclude = ['host','participants']  #as we dont want the user to select the host and participants from all user thats why we exclude it from form


class UserRegistration(forms.ModelForm):
    firstName = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter first Name'})
    lastName = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter last Name'})
    email = forms.EmailField(max_length=200,required=True,error_messages={'required':'Please enter Email'})
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(),error_messages={'required':'Please enter Your Password'})
    username = forms.CharField(max_length=50,required=True,error_messages={'required':'Please enter Username'})
    class Meta:
        model = User
        fields = ['firstName','lastName','email','password','username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already used')
        return email
    

class UserForm(forms.ModelForm):
    # bio = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['username','email']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = self.instance  # Get the current user instance

        # Check if any other user has the same email
        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            raise forms.ValidationError('Email already used by other user.')

        return email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio','profile_pic']