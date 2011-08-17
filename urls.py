from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

     url(r'^campanhas/$', 'opensocialcrm.campanhas.views.index'),
     url(r'^campanhas/nova/$', 'opensocialcrm.campanhas.views.nova'),
     url(r'^campanhas/cadastrar_nova/$', 'opensocialcrm.campanhas.views.cadastrarNova'),
     #url(r'^resultados/$', 'opensocialcrm.resultados.views.index'),
     (r'^resultados/(?P<url>\w+)/$', 'opensocialcrm.resultados.views.index'),
     #url(r'^relacionamentos/', 'crm.relacionamentos.views.index'),
     url(r'^$', 'opensocialcrm.index.views.index'),
     url(r'^erro_autenticacao/$', 'opensocialcrm.index.views.erroAutenticacao'),
     (r'^grappelli/', include('grappelli.urls')),
     (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
     (r'^static/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
     url(r'^admin/', include(admin.site.urls)),
     (r'^facebook/', include('django_facebook.urls')),
)

