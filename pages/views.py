from django.shortcuts import render

def pages_list(request):
	return render(request, 'pages/pages_list.html')


