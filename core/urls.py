from django.urls import path
from .views import HomePage

urlpatterns = [
    path("homepage", HomePage, name='homepage')
]