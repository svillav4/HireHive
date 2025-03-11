from django.urls import path
from .views import HomePageView, ShowServiceView, CreateServiceView, ServiceSuccessView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('services/', ShowServiceView.as_view(), name='show_services'),
    path('services/create', CreateServiceView.as_view(), name='create_service'),
    path('services/success', ServiceSuccessView.as_view(), name='service_success'),
]
