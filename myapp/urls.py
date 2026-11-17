from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('clients/', views.clients_view, name='clients'),
    path('employees/', views.employees_view, name='employees'),
    path('payments/', views.payments_view, name='payments'),
    path('department/', views.department_view, name='department'),
    path('materials/', views.materials_view, name='materials'),
    path('projectassignment/', views.projectassignment_view, name='projectassignment'),
    path('projects/', views.projects_view, name='projects'),
    path('supplier/', views.supplier_view, name='supplier'),
    path('clients/update/<int:id>/', views.update_client, name='update_client'),
    path('clients/delete/<int:id>/', views.delete_client, name='delete_client'),
    path('department/update/<int:id>/', views.update_department, name='update_department'),
    path('department/delete/<int:id>/', views.delete_department, name='delete_department'),
    path('employees/update/<int:id>/', views.update_employee, name='update_employee'),
    path('employees/delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('projects/update/<int:id>/', views.update_project, name='update_project'),
    path('projects/delete/<int:id>/', views.delete_project, name='delete_project'),  
    path('materials/update/<int:id>/', views.update_material, name='update_material'),
    path('materials/delete/<int:id>/', views.delete_material, name='delete_material'),   
    path('payments/update/<int:id>/', views.update_payment, name='update_payment'),
    path('payments/delete/<int:id>/', views.delete_payment, name='delete_payment'),
    path('projectassignment/update/<int:id>/', views.update_projectassignment, name='update_projectassignment'),
    path('projectassignment/delete/<int:id>/', views.delete_projectassignment, name='delete_projectassignment'), 
    path('supplier/update/<int:id>/', views.update_supplier, name='update_supplier'),
    path('supplier/delete/<int:id>/', views.delete_supplier, name='delete_supplier'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
         
     
    
]