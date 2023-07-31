from . import views
from django.urls import path

urlpatterns = [
    path('Документы/', views.listJournal, name='list'),


]