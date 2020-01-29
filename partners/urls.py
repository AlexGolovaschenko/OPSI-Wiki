from django.urls import path
from partners import views

app_name = 'partners'

urlpatterns = [
    path('', views.partners_list, name='partners_list'),
    path('contractor/detail/<int:id>', views.contractor_detail, name='contractor_detail'),
    path('contractor/add/', views.update_contractor, name='add_contractor'),
    path('contractor/update/<int:id>', views.update_contractor, name='update_contractor'),
    path('contractor/delete/<int:id>', views.delete_contractor, name='delete_contractor'),

    path('supplier/detail/<int:id>', views.supplier_detail, name='supplier_detail'),
    path('supplier/add/', views.update_supplier, name='add_supplier'),
    path('supplier/update/<int:id>', views.update_supplier, name='update_supplier'),
    path('supplier/delete/<int:id>', views.delete_supplier, name='delete_supplier'),

    path('company/comments/add/', views.leave_comment, name='leave_comment'),
    path('company/comments/delete/<int:id>', views.delete_comment, name='delete_comment'),
]
