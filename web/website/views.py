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
from website.predict_cyber import bully_analysis


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
    print(len(twitter_search[0]))
    db.child('users').child(email).set(twitter_search)


def twitter(request):
    """
    Maps the index url to the html page
    :param request: the url request
    :return: the index page if authenticated, else returns to the login page
    """

    data = {
    }
    print(request)
    if request.GET.get('TwitterKey') or request.GET.get('TwitterSecret'):
        val = request.GET.get('TwitterKey')
        secret = request.GET.get('TwitterSecret')
        email = request.GET.get('email')
        print(val, secret, email)
        # print(email)
        try:
            tweets = website.twitter_search.get_tweets(token=val, secret=secret)
        except:
            tweets = website.twitter_search.read_tweets()
        twitter_val = website.twitter_search.final_called(tweets)
        print("the prev len" + str(len(twitter_val)))
        write_to_firebase(twitter_val, email)
    return render(request, 'new-index.html', data)


def tweet(request):
    """
    Maps the index url to the html page
    :param request: the url request
    :return: the index page if authenticated, else returns to the login page
    """

    data = {
    }
    if request.GET.get('tweet'):
        tweet = request.GET.get('tweet')
        data['harass'] = bully_analysis(tweet)
        data['validity'] = "True"
        sites = open('website/file.txt', 'r')
        sitelist = json.loads(sites.read()).keys()
        for i in sitelist:
            if i in tweet:
                data['validity'] = "False"
    return render(request, 'new-index.html', data)
