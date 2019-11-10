from django.conf.urls import url
from Apptwo import views
from django.urls import path


urlpatterns = [
	path('',views.users,name='users'),
]