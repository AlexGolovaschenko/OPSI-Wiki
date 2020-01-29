from django.urls import path
from fileslibrary import views

app_name = 'fileslibrary'

urlpatterns = [
	path('', views.home, name='home'),
	path('documents/', views.regulatory_documents, name='regulatory_documents'),
	path('articles/', views.articles, name='articles'),
	path('file/add/', views.add_file, name='add_file'),
	path('file/edit/<int:id>', views.edit_file, name='edit_file'),
	path('topic/add/', views.add_topic, name='add_topic'),
	path('delete/<int:id>', views.delete_file, name='delete_file'),
]

