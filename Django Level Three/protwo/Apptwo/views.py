from django.shortcuts import render
from django.http import HttpResponse
from Apptwo.models import User
from Apptwo.forms import NewUserForm
# Create your views here.
def index(request):
	# return HttpResponse("<em>My Second App</em>")
	return render(request,'Apptwo/index.html')

def users(request):

	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('Error Form Invalid')
	return render(request,'Apptwo/users.html', {'form':form})


	# user_list = User.objects.order_by('first_name')
	# user_dict = {'users':user_list}
	# return render(request,'Apptwo/users.html',context=user_dict)


