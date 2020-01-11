from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from pages.models import Page, Category, Section
from pages.forms import PageCreateForm, SectionCreateForm, SectionInlineFormSet, \
						FileInlineFormSet, LinkInlineFormSet, ReferenceInlineFormSet

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


@login_required
def update_page(request, id=None):
	if id:
		# update existing page
		page_instance = get_object_or_404(Page, pk=id)
	else:
		# create new page
		page_instance = None

	if request.method == "POST":
		page_form = PageCreateForm(request.POST, instance = page_instance)

		if page_form.is_valid():
			page = page_form.save()

			section_forms = SectionInlineFormSet(request.POST, instance = page)
			if section_forms.is_valid():
				section_forms.save()
			else:
				messages.warning(request, f'Возникла ошибка при редактировании разделов!')

			file_forms = FileInlineFormSet(request.POST, request.FILES, instance = page)
			if file_forms.is_valid():
				file_forms.save()
			else:
				messages.warning(request, f'Возникла ошибка при сохранении файлов!')

			link_forms = LinkInlineFormSet(request.POST, instance = page)
			if link_forms.is_valid():
				link_forms.save()
			else:
				messages.warning(request, f'Возникла ошибка при сохранении ссылок!')

			reference_forms = ReferenceInlineFormSet(request.POST, instance = page)
			if reference_forms.is_valid():
				reference_forms.save()
			else:
				messages.warning(request, f'Возникла ошибка при сохранении литературы!')

			messages.success(request, f'Страница успешно изменена!')
			return redirect('pages:detail', page.id)

		else:
			messages.warning(request, f'Возникла ошибка при редактировании страницы!')
			if id:
				return redirect('pages:detail', str(id))
			else:
				return redirect('home')

	else:
		page_form = PageCreateForm(instance = page_instance)
		section_forms = SectionInlineFormSet(instance=page_instance)
		file_forms = FileInlineFormSet(instance=page_instance)
		link_forms = LinkInlineFormSet(instance=page_instance)
		reference_forms = ReferenceInlineFormSet(instance=page_instance)

		
	context = {
		'page_form': page_form,
		'section_forms': section_forms,
		'file_forms': file_forms,
		'link_forms': link_forms,
		'reference_forms': reference_forms,
		'page_id': id,
	}

	return render(request, 'pages/update_page.html', context)


@login_required
def delete_page(request, id):
	page = get_object_or_404(Page, pk=id)
	page.delete()
	messages.info(request, f'Страница удалена!')
	next = request.GET.get('next', '/')
	return HttpResponseRedirect(next)
