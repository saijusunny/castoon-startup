from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index/index.html')

######################################################################### <<<<<<<<<< CREATOR MODULE >>>>>>>>>>>>>>

def login_creator(request):
    return render(request,'index/index_creator/index_creator_login.html')

######################################################################### <<<<<<<<<< ARTIST MODULE >>>>>>>>>>>>>>>>

def login_artist(request):
    return render(request,'index/index_artist/index_artist_login.html')