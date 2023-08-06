from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views import View
from .forms import SignUpForm
from blogsite.settings import SUCCESS_SIGNUP_URL

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import transaction
from django.http import HttpResponse

class user_registration(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, "cis_DjangoSignUp/registration_form.html",{'form': form})
    
    @transaction.atomic
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            print ("here1")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            to_email = form.cleaned_data['email']
            mail_subject = 'Activate your account.'
            message = render_to_string('cis_DjangoSignUp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return JsonResponse({"message":'A verification link has been sent to your email account,Please confirm your email address to activate your account.'},status=200)
        else:
            form_errors=form.errors
            return JsonResponse({'form_errors': get_form_error(form),'is_valid':False}, status=200)

class activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            return redirect(SUCCESS_SIGNUP_URL)
            
        else:
            return HttpResponse('Activation link is invalid!')

def get_form_error(form_error):
    error_dict = dict(form_error.errors)
    error_list = [] 
    if error_dict.items():
        for field, errors in error_dict.items():
            field = str(field.replace('_',' '))
            error = ", ".join(errors)
            error_list.append("<strong>"+field.title()+"</strong> : " + str(error))
    if error_list:
        error_html = "<ul>"
        for error in error_list:
            error_html += "<li> "+ error +"</li>"
        error_html += "</ul>"
        return error_html
    return False
