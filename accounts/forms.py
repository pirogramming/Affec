from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User, Profile


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'email')

class ProfileForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = '__all__'

