from cmath import log
from http.client import HTTPException

from django.shortcuts import redirect, render

from meetups.forms import RegistrationForm

from .models import Meetup

# Create your views here.

def index(request):
	meetups = Meetup.objects.all()
	return render(request, 'meetups/index.html', { 
		'meetups' : meetups 
	})

def meetup_details(request, meetup_slug):
	selected_meetup = Meetup.objects.get(slug=meetup_slug)
	
	if(request.method == 'GET'):
		registration_form = RegistrationForm()
	else:
		registration_form = RegistrationForm(request.POST)
		if registration_form.is_valid():
			participant = registration_form.save()
			selected_meetup.participants.add(participant)
			return redirect('confirm-registration')


	return render(request, 'meetups/meetup-details.html', {'selected_meetup':selected_meetup, 'form':registration_form})

def confirm_registration(request):
	return render(request, 'meetups/registration-success.html')
