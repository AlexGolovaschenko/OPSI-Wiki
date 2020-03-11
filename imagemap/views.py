from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
def creator(request):
	return render(request, 'imagemap/index.html', context={'radius': False})

def creator_with_radius(request):
	return render(request, 'imagemap/index.html', context={'radius': True})

@xframe_options_sameorigin
def iframe_10442(request):
	return render(request, 'imagemap/10442.html')