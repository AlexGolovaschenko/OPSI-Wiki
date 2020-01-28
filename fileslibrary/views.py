from django.shortcuts import render
from fileslibrary.models import Topic, File


def library(request):
	topics = Topic.objects.all()

	contents = []
	for topic in topics:
		files = topic.file_set.all()
		if files:
			cont = {}
			cont['topic'] = topic.name
			cont['files'] = files
			contents.append(cont)

	context = {'contents': contents}
	return render(request, 'fileslibrary/library.html', context)