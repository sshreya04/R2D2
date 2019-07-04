from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from bs4 import BeautifulSoup
import requests
#from .models import 
from rest_framework import viewsets
from serializers import DetailSerializer
from .models import data
from rest_framework.decorators import api_view
from django.shortcuts import render 
from django.http import Http404
# Create your views here.
name = []

def index(request):
	list_ = data.objects.order_by('-pub_date')
	page_link ='https://www.imdb.com/chart/top?ref_=nv_mv_250'
	page_response = requests.get(page_link,timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	movie_name = page_content.find('tbody', attrs={'class':'lister-list'})
	for link in movie_name("a"):
		name.append(link.get('title'))
	return render(request , "movies/index.html" , {'name' : name})

def detail(request , movie_id):
	try:
		movie = data.objects.get(pk=movie_id)
	except data.DoesNotExist:
		raise Http404("Movie not Exist")
	return render(request , "movies/detail.html" , {'movie':movie})

class DetailViewSet(viewsets.ModelViewSet)   
    queryset = data.objects.all()
    serializer_class = DetailSerializer	



    