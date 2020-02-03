from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from PIL import Image


class Comment(models.Model):
	author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	text = models.TextField(verbose_name='Текст комментария')
	pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def object_name(self):
		if self.content_object:
			return str(self.content_object)
		else:
			return "Object has been deleted or doesn't exist"

	def __str__(self):
		return self.author.username + ': ' + 'comment...'

	class Meta():
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'


class Contractor(models.Model):
	company_name = models.CharField(max_length=200, verbose_name='Наименование организации')
	icon = models.ImageField(default='pertner_icon_default.png', upload_to='partners_icons', verbose_name='Иконка' )
	contacts = models.TextField(verbose_name='Контакты')
	service = models.TextField(verbose_name='Тип услуги, деятельность')
	examples = models.TextField(verbose_name='Примеры работ', blank = True)
	rating = models.PositiveSmallIntegerField(verbose_name='Оценка', default=0, 
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0)
		] )
	comments = GenericRelation(Comment, related_query_name='comments')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		icon = Image.open(self.icon.path)
		if icon.height > 300 or icon.width > 300:
			output_size = (300, 300)
			icon.thumbnail(output_size)
			icon.save(self.icon.path)

	def class_name(self):
		return self.__class__.__name__

	def __str__(self):
		return self.company_name

	class Meta:
		verbose_name = 'Субподрядчик'
		verbose_name_plural = 'Субподрядчики'



class Supplier(models.Model):
	company_name = models.CharField(max_length = 200, verbose_name = 'Наименование организации')
	icon = models.ImageField(default='pertner_icon_default.png', upload_to='partners_icons', verbose_name = 'Иконка')
	contacts = models.TextField(verbose_name='Контакты')
	service = models.TextField(verbose_name='Тип поставляемого оборудования')
	rating = models.PositiveSmallIntegerField(verbose_name='Оценка', default=0, 
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0)
		] )	
	comments = GenericRelation(Comment, related_query_name='comments')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		icon = Image.open(self.icon.path)
		if icon.height > 300 or icon.width > 300:
			output_size = (300, 300)
			icon.thumbnail(output_size)
			icon.save(self.icon.path)

	def class_name(self):
		return self.__class__.__name__

	def __str__(self):
		return self.company_name

	class Meta:
		verbose_name = 'Поставщик'
		verbose_name_plural = 'Поставщики'



			