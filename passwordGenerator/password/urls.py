from . import views
from django.urls import path


urlpatterns = [
    path('', views.main, name='base_page')
]