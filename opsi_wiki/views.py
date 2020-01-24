from django.shortcuts import render

def home(request):
	return render(request, 'opsi_wiki/home.html')

def about(request):
	return render(request, 'opsi_wiki/about.html')

def library(request):
	return render(request, 'opsi_wiki/library.html')
