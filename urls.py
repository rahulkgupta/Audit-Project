from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('main.views',
    (r'^$','index'),
    (r'^signin$','signin'),
    (r'^dashboard$','dashboard'),
    (r'^audits$','audits'),
    (r'^signup$','signup'),
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

