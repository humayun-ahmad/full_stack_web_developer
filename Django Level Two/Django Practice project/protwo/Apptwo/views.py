from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<em>My Second App</em>")

# Create your views here.
