from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from pages.models import Page, Category
from pages.forms import PageCreateForm

# def pages_list(request):
# 	return render(request, 'pages/pages_list.html')


def programmer_pages_list(request):
	CATEGORY_NAME = 'Программирование'
	return _render_pages_list(request, CATEGORY_NAME)

def constructor_pages_list(request):
	CATEGORY_NAME = 'Конструирование'
	return _render_pages_list(request, CATEGORY_NAME)

def project_manager_pages_list(request):
	CATEGORY_NAME = 'Управление проектами'
	return _render_pages_list(request, CATEGORY_NAME)

def circuit_engineer_pages_list(request):
	CATEGORY_NAME = 'Схемотехника'
	return _render_pages_list(request, CATEGORY_NAME)


def _render_pages_list(request, category):
	category = get_object_or_404(Category, name=category)

	topics = {}
	try:
		pages = get_list_or_404(Page.objects.order_by('topic__order'), category=category)
		for p in pages:
			try:
				topics[p.topic.name].append(p)
			except:
				topics[p.topic.name] = [p]
	except:
		pass

	context = {'topics': topics}
	return render(request, 'pages/pages_list.html', context)


def page_detail(request, id):
	page = get_object_or_404(Page, pk=id)
	context = {'page': page}
	return render(request, 'pages/page_detail.html', context)


def create_page(request):
	if request.method == "POST":
		page_form = PageCreateForm(request.POST)

		if page_form.is_valid():
			page_form.save()
			messages.success(request, f'Страница создана успешно!')
			return redirect('home')
	else:
		page_form = PageCreateForm()

	context = {
		'page_form': page_form,
	}

	return render(request, 'pages/create_page.html', context)