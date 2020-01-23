from django.shortcuts import render


def process(request):
	return render(request, 'processmap/process.html') 