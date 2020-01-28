from django import template
from django.utils.safestring import mark_safe
from fileslibrary.models import File


register = template.Library()

@register.filter()
def file_icon(file):
	i_type = 'far fa-file'

	if isinstance(file, File):
		extension = file.file_extension()
		if extension in ('doc', 'docx'):
			i_type = 'far fa-file-word'
		elif extension == 'pdf':
			i_type = 'far fa-file-pdf'
		elif extension == 'html':
			i_type = 'far fa-file-code'
		elif extension in ('xls', 'xlsx'):
			i_type = 'far fa-file-excel'
		elif extension in ('jpg', 'png', 'swg', 'gif'):
			i_type = 'far fa-file-image'
		elif extension in ('ppt', 'pptx'):
			i_type = 'far fa-file-powerpoint'

	icon = f'<i class="{i_type} pr-2"></i>'
	return mark_safe(icon)