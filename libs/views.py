from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def success(request):

    context = {
        
    }

    template = "libs/success.html"

    return render(request, template, context)

@login_required(login_url='/accounts/login/')
def form(request):

    form = SheqForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/success/')

    context = {
        "form" : form,
    }

    template = "libs/form.html"

    return render(request, template, context)

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')  