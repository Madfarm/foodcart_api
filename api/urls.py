from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.createMenuItem),
    path('<int:pk>', views.getMenuItem)
]