from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.contact_create, name='contact_create'),
    path('read/', views.contact_read, name='contact_read'),
    path('update/<int:contact_id>/', views.contact_update, name='contact_update'),
    path('delete/<int:contact_id>/', views.contact_delete, name='contact_delete'),
]