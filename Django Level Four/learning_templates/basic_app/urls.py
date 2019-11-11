from django.urls import path
from basic_app import views
from django.conf.urls import url

# Template Tagging:
app_name = 'basic_app'

urlpatterns = [
	path('relative/', views.relative,name='relative'),
	path('other/',views.other,name='other'),
]