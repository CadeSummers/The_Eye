from django.shortcuts import render
from django.http import HttpResponse

#Const list of different request categores for The_Eye
#This list is hard coded. In project, I would take tags from the front-end framework
#And use them to define categorizaiton of requests
REQUEST_CATEGORIES = ["User Authorization", "Registration", "Page Request", "Form Submission"]

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

def get_in_contact():

    #skeleton for form submission

    return HttpResponse("Let's get in Contact!")

#actual declaration of 'the_eye' function
def the_eye():
    
    pass