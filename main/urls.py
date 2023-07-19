from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('view',views.view,name = 'view'),
    path('add',views.add,name = 'add'),
    path('update',views.update,name = 'update'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee')
]
