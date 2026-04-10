from django.urls import path
from authJwt import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
