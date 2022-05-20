from django.shortcuts import render
from django.http import HttpResponse

#Const list of different request categores for The_Eye
#This list is hard coded. In project, I would take tags from the front-end framework
#And use them to define categorizaiton of requests
REQUEST_CATEGORIES = ["User Authorization", "Registration", "Page Request"]

# Create your views here.
def login_request():

    #skeleton for login page

    return HttpResponse("You're Logged in!")

def register_request():

    #skeleton for registration page

    return HttpResponse("You're registered!")


def hello():

    #skeleton for Page request

    return HttpResponse("Hello!")
#actual declaration of 'the_eye' functino
def the_eye():
    
    pass