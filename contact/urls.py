from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_create, name='contact'),
    path('list/', views.contact_read, name='contact_read'),
    path('update/<int:contact_id>/', views.contact_update, name='contact_update'),
    path('delete/<int:contact_id>/', views.contact_delete, name='contact_delete'),
]