Django sign up testing package
==============================

**Description:**

     The main motive is to upload our own package on PyPI. so for doing testing, I have
     uploaded it on this platform.

**installation:**

Just run a command on the terminal 

            pip install cis_DjangoSignUp.

In settings.py,

1. Add in the installed app

          'cis_DjangoSignUp',

 2. Add in context processor

          'cis_DjangoSignUp.context_processors.AJAX_POST',
          'cis_DjangoSignUp.context_processors.reg_form'

3. Also, set email backend to activate account 

        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 
        EMAIL_HOST_USER = ''
        EMAIL_HOST_PASSWORD = ''
        SUCCESS_SIGNUP_URL = '' 
        AJAX_POST = True  

In main urls.py :

        path('', include('cis_DjangoSignUp.url')), 

After then add it in the template where you want :

        {% include 'cis_DjangoSignUp/register.html' %}


