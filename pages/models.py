from django.db import models
from ckeditor.fields import RichTextField 

class Category (models.Model):
	name = models.CharField(verbose_name='Название', max_length=200)
	description = models.TextField(verbose_name='Описание', blank=True)
	icon = models.ImageField(default='topic_icon_default.png', upload_to='topic_icons' )
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Категория"
		verbose_name_plural = "Категории"


class Topic (models.Model):
	name = models.CharField(verbose_name='Название', max_length=200)
	description = models.TextField(verbose_name='Описание', blank=True)
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Тема"
		verbose_name_plural = "Темы"


class Page(models.Model):
	name = models.CharField(verbose_name='Название', max_length=200)
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
	topic = models.ForeignKey(Topic, verbose_name='Тема', on_delete=models.CASCADE)	
	short_description = RichTextField(verbose_name='Краткое описание', blank=True)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = "Страница"
		verbose_name_plural = "Страницы"


class Section(models.Model):
	page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE)
	headline = models.CharField(verbose_name='Оглавление', max_length=200, blank=True)
	# content = models.TextField(verbose_name='Раздел', blank=True)
	content = RichTextField(verbose_name='Раздел', blank=True)

	def __str__(self):
		return self.headline

	class Meta():
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"


class Link(models.Model):
	page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Имя', max_length=200, blank=True)
	link = models.TextField(verbose_name='Ссылка')

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = "Внешняя ссылка"
		verbose_name_plural = "Внешние ссылки"

class Reference(models.Model):
	page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Имя', max_length=200)
	link = models.TextField(verbose_name='Ссылка', blank=True)
	author = models.CharField(verbose_name='Автор', max_length=200, blank=True)
	pub_date = models.CharField(verbose_name='Дата публикации', max_length=200, blank=True)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = "Литература"
		verbose_name_plural = "Литература"