from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Statement
from .forms import ProfileForm, StatementForm
from .calculations import *


@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    statements = Statement.objects.all()
    try:
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.save()
            return redirect('index')
    else:
        form = StatementForm()
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login')
def profile(request):
    current_user=request.user
    profile =Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form': form, 'profile':profile})

@login_required(login_url='/accounts/login')
def analyze(request, statement_id):
    try:
        statement = Statement.objects.get(id = statement_id)
    except ObjectDoesNotExist:
        raise Http404
    
    convert(statement.statement.url)
    context = {'received':received, 
    'sent':sent,
    'deposited':deposited,
    'withdrawn':withdrawn,
    'paybill':paybill,
    'buy_goods':buy_goods,
    'others':others,
    'withdrawn':withdrawn,
    'withdrawals':withdrawals,
    'withdrawn2':withdrawn2,
    'charges_w':charges_w,
    'payments':payments,
    'paid':paid,
    'charges_p':charges_p,
    'airbuy':airbuy,
    'airtime':airtime,
    'foodbuy':foodbuy,
    'food':food,
    'supbuy':supbuy,
    'sup':sup,
    'uncatbuy':uncatbuy,
    'uncat':uncat,
    }
    return render(request, 'analysis.html', context)