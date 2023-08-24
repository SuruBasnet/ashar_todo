from django.urls import path
from .views import home,create

urlpatterns = [
    path('home/',home),
    path('create/',create)
]