from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import CoreTrainee
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

@require_http_methods(["GET", "POST"])
def login_check(request):
	try:
		user = CoreTrainee.objects.get(email= request.POST['username'],
									 identification_code=request.POST['password'])
	except (KeyError, CoreTrainee.DoesNotExist):

		#redisplay the question voting form 
		return render(request, 'flow_hosp_live/login.html', {
			'error_message' : "Invalid Login",
			})
	else:
		SessionStore['user_id'] = user.id

		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice is a
		# user hits the back button.
		return HttpResponseRedirect(reverse('flow_hosp_live:user_account', args=(user.id,)))

def user_account(request, trainee_id):
	if SessionStore['user_id'] == trainee_id:
		user = CoreTrainee.objects.get(pk=trainee_id)
		context = { 'user' : user}
		return render(request, 'flow_hosp_live/user_account.html', context)
	else:
		return render(request, 'flow_hosp_live/user_account.html')
		


	
	
	