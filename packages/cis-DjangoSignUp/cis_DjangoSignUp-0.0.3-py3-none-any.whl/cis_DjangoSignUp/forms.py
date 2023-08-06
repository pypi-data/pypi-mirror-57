from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm,forms.ModelForm):
	date_of_birth= forms.DateField(error_messages=({'required': 'Please let us know your Birth date',
		'invalid': 'enter birthdate in YYYY-MM-DD'}))
	username = forms.CharField(label=_("username1"), error_messages={'required': 'Please Enter username'})

	class Meta:
		model = User
		fields = ('first_name', 'last_name','date_of_birth', 'email', 'username','password1', 'password2' )