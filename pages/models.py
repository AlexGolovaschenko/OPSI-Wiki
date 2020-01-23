from django.db import models
from django.urls import reverse
import os
from ckeditor.fields import RichTextField 


class Category (models.Model):
    SOFTWARE_DEVELOPMENT = 'SOFT_DEV'
    CONSTRUCTION = 'CONSTRUCT'
    PROJECT_MANAGMENT = 'PROJ_MANAG'
    CIRCUIT_ENGINEERING = 'CIRC_ENG'
    PROCESS_SYSTEM_INTEGRATION = 'PROC_SI'

    CATEGORY_CHOICES = [
        (None, '---------'),
        (SOFTWARE_DEVELOPMENT, 'Программирование'),
        (CONSTRUCTION, 'Конструирование'),
        (PROJECT_MANAGMENT, 'Управление проектами'),
        (CIRCUIT_ENGINEERING, 'Схемотехника'),
        (PROCESS_SYSTEM_INTEGRATION, 'Процесс "Системная интеграция"'),
    ]

    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
            verbose_name='Название', unique=True )
    order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

    def __str__ (self):
        return self.get_name_display()

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_url(self):
        return Category.get_url_by_name(self.name)

    def get_url_by_name(name):
        urls = {
            Category.SOFTWARE_DEVELOPMENT : reverse('pages:programmer_pages_list'),
            Category.CONSTRUCTION : reverse('pages:constructor_pages_list'),
            Category.PROJECT_MANAGMENT : reverse('pages:project_manager_pages_list'),
            Category.CIRCUIT_ENGINEERING : reverse('pages:circuit_engineer_pages_list'),
            Category.PROCESS_SYSTEM_INTEGRATION : reverse('processmap:process'),
        }
        return urls.get(name, reverse('home'))


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
    content = RichTextField(verbose_name='Раздел', blank=True)

    def __str__(self):
        return self.headline

    class Meta():
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

def file_storage_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/uploads/files_<page.id>/<filename>
    return 'uploads/files_{0}/{1}'.format(instance.page.id, filename)

class File(models.Model):
    page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE)
    upload = models.FileField(verbose_name='Файл', upload_to=file_storage_path)
    alter_name = models.CharField(verbose_name='Переименовать файл', max_length=200, blank=True)
    comment = models.CharField(verbose_name='Комментарий', max_length=200, blank=True)

    def filename(self):
        if self.alter_name:
            return self.alter_name
        else:
            return os.path.basename(self.upload.name).replace('_', ' ')

    def __str__(self):
        return self.filename()

    class Meta():
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

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