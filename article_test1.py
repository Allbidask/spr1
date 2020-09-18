# -*- coding: utf-8-*-
import json
import requests
import datetime
import time

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article, Comments, Tretya
# Create your views here.

def index(request):
	all_articles = Article.objects.all()
	context ={
		"articles": all_articles 
		
		}
	
	
	return render(request, "article/index.html", context)

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
		"articles": Article.objects.all()
		}
	
	
	return render(request, "article/index4.html", context)
	
def index5(request):	
	cry_all = 'https://bittrex.com/api/v1.1/public/getmarketsummaries' 
	r_all = requests.get(cry_all)

	data1_all = json.loads(r_all.text)
	data2_all = data1_all["result"]
	total_par = len(data2_all)
	data3_all = data2_all[:]
	for k in data3_all:
			
		context = {
			"all_coin": data3_all
		}
	return render(request, "article/index5.html", context)	
	
