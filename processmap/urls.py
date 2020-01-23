from django.urls import path
from . import views

app_name = "processmap"

urlpatterns = [
	path('', views.process, name='process'),

]