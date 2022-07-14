from django.urls import path
from . import views

app_name = "AdminDashboard"
urlpatterns = [
    path('', views.adminView, name="index"),
    path('check/', views.checker, name="check"),
    
]