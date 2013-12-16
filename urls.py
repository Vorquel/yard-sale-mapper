from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import views 

urlpatterns = patterns('',

    url(r'^index$', views.index, name= 'index'),
    url(r'^services$', views.services, name='service'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),

    

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)