from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


####CONSTS

#definition of standard payload model
STANDARD_KEYS = ["session_id", "category", "name", "data", "timestamp"]

#Const list of different request categores for The_Eye
#This list is hard coded. In project, I would take tags from the front-end framework
#And use them to define categorizaiton of requests
REQUEST_CATEGORIES = ["User Authorization", "Registration", "Page Request", "Form Submission"]

#host implemented as const of web address application serves at, in this case a general local home ip
HOST = "127.0.0.1:8000"



# Create your views here.
def login_request(request):

    #skeleton for login page
    

    #establish a category for this kind of request. Normally, category could be inferred from payload
    category = REQUEST_CATEGORIES[0]

    return HttpResponse("You're Logged in!")

def register_request(request):

    #skeleton for registration page

    #category : Registration
    category = REQUEST_CATEGORIES[1]

    return HttpResponse("You're registered!")

def hello(request):

    #skeleton for Page request

    #Page Request category skeleton
    category = REQUEST_CATEGORIES[2]

    return HttpResponse("Hello!")

def get_in_contact(request):

    #skeleton for form submission

    #Form Submission category skeleton
    category = REQUEST_CATEGORIES[3]

    return HttpResponse("Let's get in Contact!")

#actual declaration of 'the_eye' function
#In live project environment, I would consider create a seperate file for exclusively this function
#configuring this function to take in the request, the cattegory, and a string naming the event
def the_eye(request, category, event: str):

    #get session id as session_key
    session_id = request.session.session_key

    #category is tagged in function, event correlates to name in payload

    #define data, per the payload structure, binding host to const, and setting path as the path_info attribute
    data = {"host" : HOST, "path" : request.path_info}

    #get timestamp for the event, saved as string
    timestamp = str(datetime.now())

    #TODO zip together

    
    pass