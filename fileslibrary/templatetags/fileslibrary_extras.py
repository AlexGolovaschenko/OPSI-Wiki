from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings
from urllib.parse import urljoin
from fileslibrary.models import File


register = template.Library()

@register.filter()
def file_icon(file):
	i_type = 'far fa-file'

	if isinstance(file, File):
		extension = file.file_extension()
		title = extension
		if extension in ('doc', 'docx'):
			i_type = 'far fa-file-word'
		elif extension == 'pdf':
			i_type = 'far fa-file-pdf'
		elif extension in ('htm', 'html'):
			i_type = 'far fa-file-code'
		elif extension in ('xls', 'xlsx'):
			i_type = 'far fa-file-excel'
		elif extension in ('jpg', 'png', 'swg', 'gif'):
			i_type = 'far fa-file-image'
		elif extension in ('ppt', 'pptx'):
			i_type = 'far fa-file-powerpoint'

	icon = f'<i class="w3-large {i_type} pr-2 align-self-center" title="{title}"></i>'
	return mark_safe(icon)


@register.filter()
def file_dispaly_url(file, request):
	url = f'{request.scheme}://{request.get_host()}{file.upload.url}'
	if file.file_extension() in ('ppt', 'pptx', 'doc', 'docx', 'xls', 'xlsx'):
		url = f'http://view.officeapps.live.com/op/view.aspx?src={url}'
		# url = f'https://docs.google.com/viewer?url={url}' # работает через раз но поддерживает на много больше форматов
		# https://docs.google.com/a/nasonline/viewer?url=http://www.nasonline.org/publications/biographical-memoirs/memoir-pdfs/einstein-albert.pdf
	return url