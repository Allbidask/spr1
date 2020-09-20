# -*- coding: utf-8-*-
import jsondddd
import requests
import datetime
import time
from django.contrib.auth.forms import UserCreationForm

from django.contrib import auth

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import Article, Comments, Tretya, Coin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse


from django.core import serializers
# Create your views here.
from time import gmtime, strftime
from django import forms



def index(request):
	

	all_articles_list = Article.objects.all().order_by("-article_date")
	paginator = Paginator(all_articles_list, 12)
	page = request.GET.get('startova')
	
	try:
		all_articles = paginator.page(page)
	except PageNotAnInteger:
		all_articles = paginator.page(1)
	except EmptyPage:
		all_articles = paginator.page(paginator.num_pages)
	context ={
		"articles": all_articles,
		"username": auth.get_user(request).username
	}
	return render(request, "article/index.html", context)
	
def index_login(request):
    if not request.user.is_authenticated:
        return render(request, "article/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "article/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
	
	
		
	
	
def index2(request):

	
	context ={
		"articles": Article.objects.all()
	}
	
	
	return render(request, "article/index2.html", context)
	
	
def index3(request):
	
	context ={
		"tretyas": Tretya.objects.all()
		}
	
	
	return render(request, "article/index3.html", context)

def index4(request):
	context ={
		"articles": Article.objects.all().order_by("-article_date")
		}
	
	
	return render(request, "article/index4.html", context)
	
def index5(request):	

	

	
	context = {
		"coins": Coin.objects.all()
	
		}

	return render(request, "article/index5.html", context)	
	
def index6(request):	

	

	
	context = {
		"coins": Coin.objects.all()
	
		}

	return render(request, "article/BTC-BCN.html", context)	
def index7(request):	

	

	
	context = {
		"coins": Coin.objects.all()
	
		}

	return render(request, "article/index7.html", context)	

def register(request):
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/article')
		else:
			form  = UserCreationForm()
			args = {'form': form}
			return render(request, 'article/reg_form.html', args)


			
def time_sl(request):
	for count in range(5):
		c = time.ctime()
	
	return(c)
	time.sleep(5)	

def phone_filter(request):
    if request.method == 'GET':
        queryset = PhoneNumber.objects.filter(is_deleted = False)
        phone = request.GET.get('phone')
    
        if phone:
            queryset = queryset.filter(phone__contains=phone)
    
        response = render(
            request,
            'phone-filter.html',
            {'phonenumbers':queryset}
        )
     
        return response

def flight(request, id):	

		flight = Coin.objects.get(pk = id)

		context = {
		"flight": flight,
		"coins2": Coin.objects.all(),
		
		}
		
		return render(request, "article/flight.html", context)
		
def article_full(request, id):	

		article_full = Article.objects.get(pk = id)

		context = {
		"article_full": article_full,		
		"all_article_full": Article.objects.all(),
		}


		return render(request, "article/article_full.html", context)
		
def index8(request):

	all_articles_list = Article.objects.all().order_by("-article_date")
	paginator = Paginator(all_articles_list, 5)
	page = request.GET.get('startova')
	try:
		all_articles = paginator.page(page)
	except PageNotAnInteger:
		all_articles = paginator.page(1)
	except EmptyPage:
		all_articles = paginator.page(paginator.num_pages)
	context ={
		"articles": all_articles,
		"username": auth.get_user(request).username
	}
	return render(request, "article/index8.html", context)
	
