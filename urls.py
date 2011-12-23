from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    (r'^$','index'),
    (r'^signin$','signin'),
    (r'^dashboard$','dashboard'),
    (r'^audits$','audits'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('audits.views',
    (r'^audits/new$','create_audit'),
)

urlpatterns += patterns('reports.views',
    (r'^reports/new$','create_report'),
)
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )



urlpatterns += staticfiles_urlpatterns()

