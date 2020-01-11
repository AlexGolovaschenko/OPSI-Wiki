from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('programmer/', views.programmer_pages_list, name='programmer_pages_list'),
    path('constructor/', views.constructor_pages_list, name='constructor_pages_list'),
    path('project_manager/', views.project_manager_pages_list, name='project_manager_pages_list'),
    path('circuit_engineer/', views.circuit_engineer_pages_list, name='circuit_engineer_pages_list'),
    path('detail/<int:id>', views.page_detail, name='detail'),
    path('new/', views.update_page, name='create_page'),
    path('update/<int:id>', views.update_page, name='update_page'),
]
