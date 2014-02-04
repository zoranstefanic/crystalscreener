from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import list_detail
from crystalscreener.screens.models import Screen
from django.db.models import Q


def search(request, what):
	#what = what.split()[-1]
	if what and len(what) >= 3:
		clause = Q(salt1__icontains=what)\
			   | Q(salt2__icontains=what)\
			   | Q(salt3__icontains=what)\
			   | Q(salt4__icontains=what)\
			   | Q(prec1__icontains=what)\
			   | Q(prec2__icontains=what)\
			   | Q(prec3__icontains=what)
	screen = Screen.objects.filter(clause)
	return render_to_response('screens/screen_list.html', {'object_list':screen})

def screen_list(request, name):
	#screen = Screen.objects.filter(screen_name__icontains=name)
	screen = Screen.objects.values()
	out = []
	for s in screen:
		if s['screen_name'] == name:
			out.append(s)
	out.sort()
	screen = out
	return render_to_response('screen_list.html', {'screen':screen})

def list_all_screens(request):
	val = Screen.objects.values()
	screen_names = []
	for v in val:
		if v['screen_name'] not in screen_names:
			screen_names.append(v['screen_name'])
	screen_names.sort()	
	return render_to_response('list_all_screens.html', {'screen_names':screen_names})
