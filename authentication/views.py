
from http.client import responses
from multiprocessing import AuthenticationError
from urllib import response
from django.forms import PasswordInput
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.template.loader import render_to_string
import authentication

from authentication.apps import AuthenticationConfig




# Create your views here.


def index(request):
    if request.method == 'POST':
   
        # AuthenticationForm_can_also_be_used__
   
        username = request.POST['username']
        password = request.POST['password']
        user = authentication(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationConfig()
    return render(request, 'authentication/login.html', {'form':form, 'title':'log in'})
    
    
    
def dashboard(request):
    return render(request, "authentication/dashboard.html")

def signout(request):
    pass

