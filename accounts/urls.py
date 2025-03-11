from django.urls import path
from .views import SignupView, LoginView, LogoutView, FreelancerDetailsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('freelancer_details/', FreelancerDetailsView.as_view(), name='freelancer_details'),
]