from django.urls import path
from .views import MyServicesView, CreateServiceView, ServiceSuccessView, ServiceView, EditServiceView, DeleteServiceView, CreateReviewView, CreateOrderView

urlpatterns = [
    path('my_services/', MyServicesView.as_view(), name='my_services'),
    path('create/', CreateServiceView.as_view(), name='create_service'),
    path('success/', ServiceSuccessView.as_view(), name='success'),
    path('<int:pk>/', ServiceView.as_view(), name='service_view'),
    path('edit/<int:pk>/', EditServiceView.as_view(), name='edit_service'),
    path('delete/<int:pk>/', DeleteServiceView.as_view(), name='delete_service'),
    path('order/<int:pk>', CreateOrderView.as_view(), name='create_order'),
    path('review/<int:pk>', CreateReviewView.as_view(), name='create_review'),
]

