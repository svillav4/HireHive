from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from django.db.models import Q

# Create your views here.

STATUS_COLORS = {
    'Completed': 'text_completed',
    'Cancelled': 'text_cancelled',
    'Pending Approval': 'text_pending_approval',
    'Pending Payment': 'text_pending_payment',
    'In Progress': 'text_in_progress',
}

class SeviceOrdersView(LoginRequiredMixin, View):
    template_name = 'service_orders.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, service_id):
        orders = Order.objects.filter(service_id = service_id).exclude( Q(status='Pending Approval') | Q(status='Pending Payment')).order_by('-creation_date')
        for order in orders:
            order.status_color = STATUS_COLORS.get(order.status, '')
        return render(request, self.template_name, {'orders': orders})

 
class OrdersClientView(LoginRequiredMixin, View):
    template_name = 'orders_client.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'client'):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        orders = Order.objects.filter(client__user=request.user.id).order_by('-creation_date')
        for order in orders:
            order.status_color = STATUS_COLORS.get(order.status, '')
        return render(request, self.template_name, {'orders': orders})
    
    def post(self, request, id):
        Order.objects.filter(id=id).update(status="In Progress")
        return redirect('orders_client')
    
class OrdersFreelancerView(LoginRequiredMixin, View):
    template_name = 'orders_freelancer.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        orders = Order.objects.filter(service__freelancer__user=request.user.id).filter(Q(status='Pending Approval') | Q(status='Pending Payment')).order_by('-creation_date')
        orders_pending_approval = []
        orders_pending_payment = []
        for order in orders:
            order.status_color = STATUS_COLORS.get(order.status, '')
            if order.status == 'Pending Approval':
                orders_pending_approval.append(order)
            else:
                orders_pending_payment.append(order)
        return render(request, self.template_name, {'orders_pending_approval': orders_pending_approval, 'orders_pending_payment': orders_pending_payment})    
    
    def post(self, request, id):

        action = request.POST.get("action")  # Detectar qué botón se presionó
        if action == "accept":
            Order.objects.filter(id=id).update(status="Pending Payment")
        elif action == "decline":
            Order.objects.filter(id=id).update(status="Cancelled")
        return redirect('orders_freelancer')