import os
import mimetypes
from wsgiref.util import FileWrapper
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.utils.encoding import smart_str
from website.forms import UserForm, VideosForm
from website.models import Video
import hashlib


# from celery import result.AsyncResult.ready



def index(request):
    """
    Maps the index url to the html page
    :param request: the url request
    :return: the index page if authenticated, else returns to the login page
    """

    data = {
    }
    if request.GET.get('Error_Message'):
        test = request.GET.get('Error_Message')
        data['error'] = test
    return render(request, 'index.html', data)

def twitter(request):
    """
    Maps the index url to the html page
    :param request: the url request
    :return: the index page if authenticated, else returns to the login page
    """

    data = {
    }
    if request.POST.get('TwitterKey') and request.POST.get('TwitterSecret'):
        test = request.GET.get('Error_Message')
        data['error'] = test
    return render(request, 'index.html', data)
