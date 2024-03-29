from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('main.views',
    (r'^$','index'),
    (r'^signin$','signin'),
    (r'^dashboard$','dashboard'),
    (r'^audits$','audits'),
    (r'^signup$','signup'),
    (r'^join$','join'),
    (r'^teams$','teams'),
    (r'^teams/(\w+)$','team'),
    (r'^accept_member/(\d+)$','accept_member'),
    (r'^deny_member/(\d+)$','deny_member'),

)

urlpatterns += patterns('main.views',
    (r'^teams_create$','create_org'),
    (r'^teams_join$','join_org'),
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

