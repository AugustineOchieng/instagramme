from django.conf.urls import url
from . import views as user_views

urlpatterns=[
    
    url(r'^$',user_views.register, name='register')
    
]