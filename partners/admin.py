from django.contrib import admin
from partners.models import Contractor, Supplier, Comment

admin.site.register(Contractor)
admin.site.register(Supplier)


class CommentAdmin (admin.ModelAdmin):
	list_display = ['__str__', 'object_name']

admin.site.register(Comment, CommentAdmin)