from django.urls import path
from fileslibrary import views

app_name = 'fileslibrary'

urlpatterns = [
	path('', views.library, name='home'),
]

