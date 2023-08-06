# from django.urls import path,re_path,include
from django.conf.urls import url
from .views import user_registration,activate

urlpatterns = [
    url(r'^user_registration', user_registration.as_view(), name = 'user_registration'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate.as_view(), name='activate'),   
    ]