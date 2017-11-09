from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import CoreTrainee, CoreExternaltraining, CoreCompany
from django.views.decorators.http import require_http_methods
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.
def index(request):
	test_list_for_index = ["how are you?", "this is for the flow page"]
	context = {
		'test_list_for_index' : test_list_for_index,
	}
	return render(request, 'flow_hosp_live/index.html', context)

def login(request):
	return render(request, 'flow_hosp_live/login.html')

# only allows GET or POST methos
@require_http_methods(["GET", "POST"])
def login_check(request):
	"""
		Takes a request arg. 
		This view is activated using the POST method.
		checks if the post Username(email) and password(identification_code) values 
		exists in the database. if the user doesn't exist user is redircted to the login
		page with an error message("Invalid login") else the user is directed to the
		user_account Url
	"""
	try:
		user = CoreTrainee.objects.get(email= request.POST['username'],
									 identification_code=request.POST['password'])
	except (KeyError, CoreTrainee.DoesNotExist):

		#redisplay the question voting form 
		return render(request, 'flow_hosp_live/login.html', {
			'error_message' : "Invalid Login",
			})
	else:
		#TODO add Sessions
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice is a
		# user hits the back button.
		return HttpResponseRedirect(reverse('flow_hosp_live:dashboard', args=(user.id,)))
  
def dashboard(request,  trainee_id):
	"""
		This is view for the user account 
		Takes a request and user id as an arg. 
		renders it to the user_account page 
	"""
	#TODO add try and catch 
	#TODO add sessions check 
	#TODO add test.py
	#TODO template doesn't exist try catch
	user = CoreTrainee.objects.get(pk=trainee_id)
	context = { 'user' : user}

	return render(request, 'flow_hosp_live/dashboard.html', context)


def company(request,trainee_id):
	"""
		This is view for the user account 
		Takes a request and user id as an arg. 
		renders it to the user_account page 
	"""
	#TODO add try and catch 
	#TODO add sessions check 
	#TODO add test.py
	#TODO template doesn't exist try catch
	user = CoreTrainee.objects.get(pk=trainee_id)
	context = { 'user' : user}
	
	return render(request, 'flow_hosp_live/company.html', context)


		
def external_training(request, trainee_id):
	"""
		This is view for the company account 
		Takes a request and user id as an arg. 
		renders it to the company page 
	"""
	#TODO add try and catch 
	#TODO add sessions check
	#TODO add test.py 
	user = CoreTrainee.objects.get(pk=trainee_id)
	external_training = CoreExternaltraining.objects.filter(company_id = user.branch.company.id)
	providers = external_training.values('provider').distinct()
	training_types = external_training.values('training_type').distinct()

	context = { 
		'user' : user,
		'external_training': external_training,
		'providers' : providers,
		'training_types' : training_types
		}
	return render(request, 'flow_hosp_live/external_training.html', context)

