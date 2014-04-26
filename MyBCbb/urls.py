from django.conf.urls import include, url, patterns
from django.contrib import admin
from MyBCbb import settings

admin.autodiscover()

urlpatterns = patterns('', 
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('img_upload.urls')),
)


##IGNORE - DEBUG
# Admin static for heroku
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
 )

## Serve user uploaded files
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )