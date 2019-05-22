from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # url(r'^$', views.home, name='instahomepage'),
    
    url(r'^$',views.feeds,name='instahomepage'),
    url(r'^profile/$',views.profile,name = 'NewProfile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit_profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^new/post/$', views.new_post, name='new_post'),
    url(r'^comments/$',views.comments,name = 'comments'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^find_profile/(\d+)',views.find_profile,name = 'find_profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)