from cmath import log
from http.client import HTTPException

from django.shortcuts import render

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
	registration_form = RegistrationForm()
	return render(request, 'meetups/meetup-details.html', {'selected_meetup':selected_meetup, 'form':registration_form})
