from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    ###################################################################################<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>>>>
    path('', views.index, name='index'),

    ################################################################################### <<<<<<<<< CREATOR MODULE >>>>>>>>>>>>>>>>>
    
    path('login_creator',views.login_creator, name='login_creator'),

    ################################################################################### <<<<<<<<< Artist MODULE >>>>>>>>>>>>>>>>>
    
    path('login_artist',views.login_artist, name='login_artist'),

    
    ]