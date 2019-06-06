from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'index.html', locals())
