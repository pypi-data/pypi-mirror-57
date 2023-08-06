from django.conf import settings
from .forms import SignUpForm

def AJAX_POST(request):
	return {'AJAX_POST':settings.AJAX_POST}

def reg_form(request):
	form = SignUpForm()
	return {'form':form}