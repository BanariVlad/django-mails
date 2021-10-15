from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('destroy/<int:mail_id>', views.destroy, name='destroy'),
    path('read/<int:mail_id>', views.read, name='read'),
]
