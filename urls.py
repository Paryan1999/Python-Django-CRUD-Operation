from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.employee_list,name='employee_list'),
    path('', views.employee_form,name='employee_insert'),
    path('<int:id>/', views.employee_form,name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    
]
