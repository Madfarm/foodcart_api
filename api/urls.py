from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuItemList),
    path('<int:pk>', views.getMenuItem)
]