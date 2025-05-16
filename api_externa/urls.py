from django.urls import path
from .views import external_products_view

urlpatterns = [
    path('', external_products_view, name='external_products'),
]
