import os
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
from django.utils.deconstruct import deconstructible
from django.conf import settings


class Video(models.Model):
    """
    The video class which holds the image the user uploaded,
     the name of the video,
    the reference to the user used.
    """
    user = models.ForeignKey(User, default=1)
    video_title = models.CharField(max_length=500000)
    video_logo = models.FileField()
    promo_code = models.CharField(max_length=500000)

    def __str__(self):
        return self.video_title

    def get_input_url(self):
        """
        The input url for the FFMPEG
        :return: The input url for the FFMPEG
        """
        return settings.PROJECT_DIR + self.video_logo.url

    def get_output_url(self):
        """
        The output url for the FFMPEG
        :return: The output url for the FFMPEG
        """
        return settings.PROJECT_DIR + self.video_logo.url.split('.')[0] + '.mp4'
