# All are imported riht now

from django.conf.urls import url
from first_app import views
from django.urls import path

# mapping with index.html file:
urlpatterns = [
	path('',views.index,name='index')
]