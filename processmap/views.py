from django.shortcuts import render
from pages.views import _get_pages_list_context
from pages.models import Category

def process(request):
	context = _get_pages_list_context(Category.PROCESS_SYSTEM_INTEGRATION)
	return render(request, 'processmap/process.html', context) 