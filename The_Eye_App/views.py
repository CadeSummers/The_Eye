from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from sys import _getframe

####CONSTS

#definition of standard payload model
STANDARD_KEYS = ["session_id", "category", "name", "data", "timestamp"]

#Const list of different request categores for The_Eye
#This list is hard coded. In project, I would take tags from the front-end framework
#And use them to define categorizaiton of requests
REQUEST_CATEGORIES = ["User Authorization", "Registration", "Page Request", "Form Submission"]

#host implemented as const of web address application serves at, in this case a general local home ip
HOST = "127.0.0.1:8000"

#global

#Empty variable for the database configuration. As this is a skeleton Django project, in a live project environement, this could represent 
#One of the numerous SQL style database configurations or any other db required/desired. Here it will be a simple dictionary
database_placeholder = {}

#####View functions

# Create your views here.
def login_request(request):

    #skeleton for login page

    #establish a category for this kind of request. Normally, category could be inferred from payload
    category = REQUEST_CATEGORIES[0]

    #grab this functions name
    event = _getframe(0).f_code.co_name

    #and utilize 'the_eye'
    database_placeholder[event] = the_eye(request, category, event)

    return HttpResponse("You're Logged in!")

def register_request(request):

    #skeleton for registration page

    #category : Registration
    category = REQUEST_CATEGORIES[1]

    #grab this functions name
    event = _getframe(0).f_code.co_name

    #and utilize 'the_eye'
    database_placeholder[event] = the_eye(request, category, event)

    return HttpResponse("You're registered!")

def hello(request):

    #skeleton for Page request

    #Page Request category skeleton
    category = REQUEST_CATEGORIES[2]

    #grab this functions name
    event = _getframe(0).f_code.co_name

    #and utilize 'the_eye'
    database_placeholder[event] = the_eye(request, category, event)

    return HttpResponse("Hello!")

def get_in_contact(request):

    #skeleton for form submission

    #Form Submission category skeleton
    category = REQUEST_CATEGORIES[3]

    #grab this functions name
    event = _getframe(0).f_code.co_name

    #and utilize 'the_eye'
    database_placeholder[event] = the_eye(request, category, event)

    return HttpResponse("Let's get in Contact!")

#actual declaration of 'the_eye' function
#In live project environment, I would consider create a seperate file for exclusively this function
#This fucntion is configured to take in the request, the category, and a string naming the event
def the_eye(request, category, event: str):

    #get session id as session_key
    session_id = request.session.session_key

    #category is tagged in function, event correlates to name in payload

    #define data, per the payload structure, binding host to const, and setting path as the path_info attribute
    data = {"host" : HOST, "path" : request.path_info}

    #get timestamp for the event, saved as string
    timestamp = str(datetime.now())

    #convert above variables and arguments into list format
    event_values = [session_id, category, event, data, timestamp]

    #if missing a value
    if None in event_values:
        
        #Print error message to server and return failure
        print("ERROR, event payload data missing")
        return -1

    #and create dict with standard keys and event values
    event_dict = {STANDARD_KEYS[i]: event_values[i] for i in range(5)}

    #tie this event to the requester's session (parallel session holding to database_placeholder)
    request.session[event] = event_dict

    #return object, normally this would be returned to database architecture
    return event_dict


