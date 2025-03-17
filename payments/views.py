from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order

# Create your views here.

STATUS_COLORS = {
    'Completed': 'text_completed',
    'Cancelled': 'text_cancelled',
    'Pending Approval': 'text_pending_approval',
    'In Progress': 'text_in_progress',
}

class JobApplicationView(LoginRequiredMixin, View):
    template_name = 'job_application.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, service_id):
        jobApplications = Order.objects.filter(service_id = service_id).order_by('-creation_date')
        for jobApplication in jobApplications:
            jobApplication.status_color = STATUS_COLORS.get(jobApplication.status, '')
        return render(request, self.template_name, {'jobApplications': jobApplications})

 
class MyHiresView(LoginRequiredMixin, View):
    template_name = 'my_hires.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'client'):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        orders = Order.objects.filter(client__user=request.user.id).order_by('-creation_date')
        for order in orders:
            order.status_color = STATUS_COLORS.get(order.status, '')
        return render(request, self.template_name, {'orders': orders})