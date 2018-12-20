
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='mnist/index.html'), name='index'),
    path('upload/', views.upload, name='upload'),
]
