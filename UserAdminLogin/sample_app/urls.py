from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_page'),
    path('signup/', views.signup, name='signup_page'),
    path('signout/', views.signout, name='signout'),
    path('adminsignout/', views.adminsignout, name='adminsignout'),
    path('Home/', views.home, name='home_page'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),  
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
]
