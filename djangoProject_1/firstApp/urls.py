from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('login/', views.login, name='login'),
    path('loginlog/', views.loginlog, name='loginlog'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('editrecord/<int:id>', views.editrecord, name='editrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
]