from django.db import models
import os


class Topic(models.Model):
	REGULATORY_DOCUMENTS = 'RD'
	ARTICLES = 'AR'

	TOPIC_CATEGORI_CHOICES = [
		(REGULATORY_DOCUMENTS, 'Нормативная документация'),
		(ARTICLES, 'Литература'),
	]

	category = models.CharField(max_length=10, choices=TOPIC_CATEGORI_CHOICES, verbose_name='Категория')
	name = models.CharField(max_length=100, verbose_name='Название')

	def __str__(self):
		return self.get_category_display() + ': ' + self.name

	class Meta:
		verbose_name = 'Тема'
		verbose_name_plural = 'Темы'



def file_storage_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/fileslibrary/topic_<topic.id>/<filename>
	return 'fileslibrary/topic_{0}/{1}'.format(instance.topic.id, filename)

class File(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
	upload = models.FileField(upload_to=file_storage_path, verbose_name='Файл', max_length=500)
	alter_name = models.CharField(verbose_name='Переименовать файл', max_length=200, blank=True)
	description = models.TextField(verbose_name='Описание', blank=True)

	def file_extension(self):
		return self.upload.name.split('.')[-1].lower()

	def file_name(self):
		if self.alter_name:
			return self.alter_name
		else:
			return os.path.basename(self.upload.name).replace('_', ' ')

	def __str__ (self):
		return self.file_name()

	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'