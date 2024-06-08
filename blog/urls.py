from . import views
from django.urls import path

urlpatterns = [
    path('', views.postList.as_view(), name='home')
]