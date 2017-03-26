import os
import mimetypes
from wsgiref.util import FileWrapper
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.utils.encoding import smart_str
import hashlib
import website.twitter_search
# from firebase import firebase
import requests
import json
import pyrebase


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


def write_to_firebase(twitter_search, email):
    config = {
        'apiKey': "AIzaSyD1E7AjUW-wfEEpYphcqgEE9MGZFJBENzY",
        'authDomain': "hshacks3-7dc18.firebaseapp.com",
        'databaseURL': "https://hshacks3-7dc18.firebaseio.com",
        'storageBucket': "hshacks3-7dc18.appspot.com",
        'messagingSenderId': "1015361765033"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child('users').child(email).set(twitter_search)


def twitter(request):
    """
    Maps the index url to the html page
    :param request: the url request
    :return: the index page if authenticated, else returns to the login page
    """

    data = {
    }
    if request.GET.get('TwitterKey') or request.GET.get('TwitterSecret'):
        val = request.GET.get('TwitterKey')
        secret = request.GET.get('TwitterSecret')
        email = request.GET.get('email')
        print(email)
        try:
            tweets = website.twitter_search.get_tweets()
        except:
            tweets = website.twitter_search.read_tweets()
        twitter_val = website.twitter_search.final_called(tweets)
        write_to_firebase(twitter_val, email)
    return render(request, 'new-index.html', data)
