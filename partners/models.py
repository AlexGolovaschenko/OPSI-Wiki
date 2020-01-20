from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

class Contractor(models.Model):
	company_name = models.CharField(max_length=200, verbose_name='Наименование организации')
	icon = models.ImageField(default='topic_icon_default.png', upload_to='partners_icons', verbose_name='Иконка' )
	contacts = models.TextField(verbose_name='Контакты')
	service = models.CharField(max_length=200, verbose_name='Тип услуги, деятельность')
	examples = models.TextField(verbose_name='Примеры работ')
	rating = models.PositiveSmallIntegerField(verbose_name='Оценка', default=0, 
		validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ] )

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	def __str__(self):
		return 'contractor'

	class Meta:
		verbose_name = 'Субподрядчик'
		verbose_name_plural = 'Субподрядчики'



class Supplier(models.Model):
	company_name = models.CharField(max_length = 200, verbose_name = 'Наименование организации')
	icon = models.ImageField(default='topic_icon_default.png', upload_to='partners_icons', verbose_name = 'Иконка')
	contacts = models.TextField(verbose_name = 'Контакты')
	service = models.CharField(max_length = 200, verbose_name = 'Тип поставляемого оборудования')
	rating = models.PositiveSmallIntegerField(verbose_name='Оценка', default=0, 
		validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ] )	

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	def __str__(self):
		return 'contractor'

	class Meta:
		verbose_name = 'Поставщик'
		verbose_name_plural = 'Поставщики'