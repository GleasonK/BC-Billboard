from django.conf.urls import patterns, url

from img_upload import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    # using as view
    # url(r'^helloC/$',  views.HelloTemplate.as_view(), name='HelloC'),
)