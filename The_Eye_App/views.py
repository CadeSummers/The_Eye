from django.shortcuts import render
from django.http import HttpResponse

#Const list of different request categores for The_Eye
#This list is hard coded. In project, I would take tags from the front-end framework
#And use them to define categorizaiton of requests
REQUEST_CATEGORIES = ["User Authorization", "Registration", "Page Request", "Form Submission"]

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
    
    pass