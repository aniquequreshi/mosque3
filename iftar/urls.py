from django.urls import path, reverse
from . import views

app_name = 'iftar'

urlpatterns = [
    path('', views.DonorCreate.as_view(), name='create'),
    path('list/', views.IndexView.as_view(), name= 'index'),
]