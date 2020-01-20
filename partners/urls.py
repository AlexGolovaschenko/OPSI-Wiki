from django.urls import path
from partners import views

app_name = 'partners'

urlpatterns = [
    path('', views.partners_list, name='partners_list'),
    path('detail/<int:id>', views.partners_detail, name='detail'),
]
