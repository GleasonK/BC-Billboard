from django.conf.urls import patterns, url

from img_upload import views

urlpatterns = patterns('',
    url(r'^test/$', views.IndexView.as_view(), name='index'),
    
    # using as view
    # url(r'^helloC/$',  views.HelloTemplate.as_view(), name='HelloC'),
)