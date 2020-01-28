from django.contrib import admin
from fileslibrary.models import Topic, File


class FileInline(admin.TabularInline):
	model = File
	extra = 1


class TopicAdmin (admin.ModelAdmin):
	inlines = [FileInline]

admin.site.register(Topic, TopicAdmin)