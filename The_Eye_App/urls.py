from django.urls import path
from . import views

#creation of basic paths
urlpatterns = [

    path('login_request/', views.login_request), 

    path('register_request/', views.register_request),

    path('hello/', views.hello),

    path('form_submit/', views.get_in_contact)

]