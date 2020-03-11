from django.shortcuts import render

# Create your views here.
def creator(request):
	return render(request, 'imagemap/index.html', context={'radius': False})

def creator_with_radius(request):
	return render(request, 'imagemap/index.html', context={'radius': True})

def iframe_10442(request):
	return render(request, 'imagemap/10442.html')