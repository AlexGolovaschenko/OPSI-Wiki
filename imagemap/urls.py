from django.urls import path
from . import views

app_name = "imagemap"

urlpatterns = [
	path('', views.creator, name='creator'),
	path('with-radius/', views.creator_with_radius, name='creator_with_radius'),
	path('10442/', views.iframe_10442, name='10442'),

]