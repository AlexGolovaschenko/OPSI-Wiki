from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from fileslibrary.models import Topic, File
from fileslibrary.forms import FileAddForm, TopicAddForm


def home(request):
	return render(request, 'fileslibrary/home.html')


def regulatory_documents(request):
	context = _get_topic_contents(Topic.REGULATORY_DOCUMENTS)
	return render(request, 'fileslibrary/files_list.html', context)


def articles(request):
	context = _get_topic_contents(Topic.ARTICLES)
	return render(request, 'fileslibrary/files_list.html', context)


def _get_topic_contents(category):
	topics = Topic.objects.filter(category = category)

	contents = []
	for topic in topics:
		files = topic.file_set.all()
		if files:
			cont = {}
			cont['topic'] = topic.name
			cont['files'] = files
			contents.append(cont)

	return {'contents': contents}



@permission_required('pages.change_page')
def add_file(request):
	if request.method == "POST":
		file_form = FileAddForm(request.POST, request.FILES)
		if file_form.is_valid():
			file_form.save()
			messages.success(request, 'Файл успешно сохранен!')
		else:
			messages.warning(request, 'Возникла ошибка при сохранении файла!')
		next = request.POST.get('next', reverse('fileslibrary:home'))
		return HttpResponseRedirect(next)
	else:
		file_form = FileAddForm()

	next = request.GET.get('next', reverse('fileslibrary:home'))	
	context = {'form':file_form, 'next': next}
	return render(request, 'fileslibrary/file_add_form.html', context)


@permission_required('pages.change_page')
def edit_file(request, id):
	instance = get_object_or_404(File, pk=id)
	if request.method == "POST":
		file_form = FileAddForm(request.POST, request.FILES, instance = instance)
		if file_form.is_valid():
			file_form.save()
			messages.success(request, 'Файл успешно сохранен!')
		else:
			messages.warning(request, 'Возникла ошибка при сохранении файла!')
		next = request.POST.get('next', reverse('fileslibrary:home'))
		return HttpResponseRedirect(next)
	else:
		file_form = FileAddForm(instance = instance)
	
	next = request.GET.get('next', reverse('fileslibrary:home'))
	context = {'form':file_form, 'next': next}
	return render(request, 'fileslibrary/file_edit_form.html', context)


@permission_required('pages.change_page')
def delete_file(request, id):
	file = get_object_or_404(File, pk=id)
	name = file.file_name()
	file.delete()
	messages.info(request, f'Документ "{name}" удален!')
	next = request.GET.get('next', reverse('fileslibrary:home'))
	return HttpResponseRedirect(next)


@permission_required('pages.change_page')
def add_topic(request):
	if request.method == "POST":
		topic_form = TopicAddForm(request.POST, request.FILES)
		if topic_form.is_valid():
			topic_form.save()
			messages.success(request, 'Тема успешно создана!')
		else:
			messages.warning(request, 'Возникла ошибка при создании темы!')
		next = request.POST.get('next', reverse('fileslibrary:home'))
		return HttpResponseRedirect(next)
	else:
		topic_form = TopicAddForm()
		
	next = request.GET.get('next', reverse('fileslibrary:home'))
	context = {'form':topic_form, 'next': next}
	return render(request, 'fileslibrary/topic_add_form.html', context)