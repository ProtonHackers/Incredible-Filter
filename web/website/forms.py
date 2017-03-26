from django import forms
from django.contrib.auth.models import User
from .models import Video

CHOICES = [('defaultKey', 'default')]


class VideosForm(forms.ModelForm):
    """
    The form used to create a video
    """
    class Meta(object):
        """
        The fields used when creating the video form
        """
        model = Video
        fields = ["video_title", 'video_logo']


class UserForm(forms.ModelForm):
    """
    The form used to create a User
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(object):
        """
        The fields in the User form
        """
        model = User
        fields = ['username', 'email', 'password']
