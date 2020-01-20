from django.shortcuts import render
from django.http import HttpResponse


def partners_list(request):
	return render(request, 'partners/partners_list.html')

def partners_detail(request, id):
	return HttpResponse('Подробно о партнере')