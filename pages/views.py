from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404
from pages.models import Page, Category, Section
from pages.forms import PageCreateForm, SectionCreateForm, getSectionInlineFormSet

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
		
		if page_form.is_valid() :
			page = page_form.save()

			section_forms = getSectionInlineFormSet()(request.POST, instance = page)
			if section_forms.is_valid():
				section_forms.save()
			else:
				messages.warning(request, f'Возникла ошибка при создании раздела!')

			messages.success(request, f'Страница успешно создана!')
			return redirect('pages:detail', page.id)
		else:
			messages.warning(request, f'Возникла ошибка при создании страницы!')
			return redirect('home')
	else:
		page_form = PageCreateForm()
		section_forms = getSectionInlineFormSet()()
		
	context = {
		'page_form': page_form,
		'section_forms' : section_forms,
	}

	return render(request, 'pages/update_page.html', context)


def update_page(request, id):
	page = get_object_or_404(Page, pk=id)

	if request.method == "POST":
		page_form = PageCreateForm(request.POST, instance = page)
		section_forms = getSectionInlineFormSet(can_delete=True)(request.POST, instance = page)

		if page_form.is_valid() and section_forms.is_valid():
			page_form.save()
			section_forms.save()
			messages.success(request, f'Страница успешно изменена!')
		else:
			messages.warning(request, f'Возникла ошибка при редактировании страницы!')
		return redirect('pages:detail', str(id))
	else:
		page_form = PageCreateForm(instance = page)
		section_forms = getSectionInlineFormSet(can_delete=True)(instance=page)
		
	context = {
		'page_form': page_form,
		'section_forms' : section_forms,
		'page_id': id
	}

	return render(request, 'pages/update_page.html', context)