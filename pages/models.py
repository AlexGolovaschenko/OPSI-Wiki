from django.db import models


class Topic (models.Model):
	name = models.CharField(verbose_name='Название', max_length=200)
	description = models.TextField(verbose_name='Описание')
	icon = models.ImageField(default='topic_icon_default.png', upload_to='topic_icons' )
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Тема"
		verbose_name_plural = "Темы"


class Page(models.Model):
	name = models.CharField(verbose_name='Название', max_length=200)
	topic = models.ForeignKey(Topic, verbose_name='Тема', on_delete=models.CASCADE)
	short_description = models.TextField(verbose_name='Краткое описание', blank=True)
	section_literature = models.TextField(verbose_name='Раздел литература', blank=True)
	section_links = models.TextField(verbose_name='Раздел ссылки', blank=True)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = "Страница"
		verbose_name_plural = "Страницы"


class Section(models.Model):
	page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE)
	headline = models.CharField(verbose_name='Оглавление', max_length=200, blank=True)
	content = models.TextField(verbose_name='Раздел', blank=True)

	def __str__(self):
		return self.headline

	class Meta():
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"