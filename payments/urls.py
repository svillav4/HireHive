from django.urls import path
from .views import JobApplicationView, MyHiresView

urlpatterns = [
    path('job_application/<int:service_id>/', JobApplicationView.as_view(), name='job_application'),
    path('my_hires/', MyHiresView.as_view(), name='my_hires'),
]