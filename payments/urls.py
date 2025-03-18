from django.urls import path
from .views import SeviceOrdersView, OrdersClientView, OrdersFreelancerView

urlpatterns = [
    path('ServiceOrders/<int:service_id>/', SeviceOrdersView.as_view(), name='service_orders'),
    path('OrdersClient/', OrdersClientView.as_view(), name='orders_client'),
    path('OrdersFreelancer/', OrdersFreelancerView.as_view(), name='orders_freelancer'),   
]