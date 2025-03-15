from django.urls import path
from .views import MyServicesView, CreateServiceView, ServiceSuccessView, ServiceView

urlpatterns = [
    path('my_services', MyServicesView.as_view(), name='my_services'),
    path('create', CreateServiceView.as_view(), name='create_service'),
    path('success', ServiceSuccessView.as_view(), name='success'),
    path('<int:id>', ServiceView.as_view(), name='service_view'),
]
