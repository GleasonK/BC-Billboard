from django.conf.urls import patterns, url

from img_upload import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^events/$', views.IndexView.as_view(), name='index'),
    url(r'^events/create$', views.create_event, name='create'),
    # using as view
    # url(r'^helloC/$',  views.HelloTemplate.as_view(), name='HelloC'),
)