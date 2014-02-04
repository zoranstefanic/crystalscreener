from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from crystalscreener.screens.views import *
from crystalscreener.screens.models import *
import os
from settings import *

site_media = os.path.join(os.path.dirname(__file__), 'site_media')
jpgs = os.path.join(os.path.dirname(__file__), 'jpgs')

screen_info = {
	'queryset' : Screen.objects.all(),
	'extra_context' : {'is_paginated': True}
}

urlpatterns = patterns('',
	# Site_media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media }),
    (r'^jpgs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': jpgs }),

	# Screen	
	#	(r'^screens/$', list_detail.object_list, screen_info),
	(r'^screens/$', list_all_screens ),
    (r'^screens/(?P<name>\w+)$', screen_list),
	
	# Search
	(r'search/(?P<what>.*)', search),
    
	# Admin
    (r'^admin/', include('django.contrib.admin.urls')),
)
