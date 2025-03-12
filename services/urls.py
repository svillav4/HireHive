from django.urls import path
from .views import HomePageView, MyServicesView, CreateServiceView, ServiceSuccessView, ManageServiceView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('services/', MyServicesView.as_view(), name='my_services'),
    path('services/create', CreateServiceView.as_view(), name='create_service'),
    path('services/success', ServiceSuccessView.as_view(), name='success'),
    path('services/manage', ManageServiceView.as_view(), name='manage_service'),
]
