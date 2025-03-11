from django.urls import path
from .views import HomePageView, MyServicesView, CreateServiceView, ServiceSuccessView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('services/', MyServicesView.as_view(), name='my_services'),
    path('services/create', CreateServiceView.as_view(), name='create_service'),
    path('services/success', ServiceSuccessView.as_view(), name='service_success'),
]
