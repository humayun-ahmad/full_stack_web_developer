from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	# return HttpResponse("Hello World!")
	my_dict = {'insert_me': "Hello I am coming form first_app/views.py!"}
	return render(request,'first_app/index.html', context = my_dict)

# Create your views here.
