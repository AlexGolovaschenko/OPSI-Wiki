from django.shortcuts import render

def library(request):
	context = {}
	return render(request, 'fileslibrary/library.html', context)