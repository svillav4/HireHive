from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.views import View
from .forms import ServiceForm
from .models import Service, Review, Category
from payments.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

class HomePageView(View):
    template_name = 'pages/home.html'

    def get(self, request):
        search = request.GET.get('search', '').strip()  # Get search query
        services = Service.objects.all()

        # Filter services by search query
        if search:
            services = Service.objects.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            ).distinct()

        # Filter services by price range
        price_filter = request.GET.get('price_filter')
        if price_filter == 'basic':
            services = services.filter(price__lte=100)
        elif price_filter == 'midrange':
            services = services.filter(price__gte=100, price__lte=400)
        elif price_filter == 'highend':
            services = services.filter(price__gte=400)

        # Filter services by category
        category_filter = request.GET.get('category_filter')
        if category_filter and category_filter != 'all':
            try:
                category_filter = int(category_filter)
                services = services.filter(category=category_filter)
            except ValueError:
                category_filter = None

        categories = Category.objects.all()

        context = {
            'services': services,
            'search': search,
            'categories': categories,
            'price_filter': price_filter,
            'category_filter': category_filter,
        }
        return render(request, self.template_name, context)


class MyServicesView(LoginRequiredMixin, View):
    template_name = 'services/my_services.html'

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        freelancer = request.user.freelancer
        services = Service.objects.filter(freelancer=freelancer)
        return render(request, self.template_name, {"services": services})
        


class CreateServiceView(LoginRequiredMixin, View):
    template_name = 'services/create_service.html'

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = ServiceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.freelancer = request.user.freelancer
            service.save()
            return redirect('success')
        
        context = {'form': form}
        return render(request, self.template_name, context)


class ServiceSuccessView(TemplateView):
    template_name = 'services/success.html'


class ServiceView(View):
    template_name = 'services/service_view.html'

    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        
        orders_in_queue = Order.objects.filter(
            service=service,
            status__in=[
                Order.Status.PENDING_PAYMENT,
                Order.Status.IN_PROGRESS
            ]
        ).count()

        reviews = Review.objects.filter(service=service).order_by('-creation_date')
        showed_reviews = reviews[:3]

        for review in showed_reviews:
            review.creation_date = review.creation_date.strftime('%b %d, %Y')
        
        # Calculate the average rating
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            average_rating = total_rating / reviews.count()
            service.rating = round(average_rating, 1)
            service.save()

        context = {
            'service': service,
            'orders_in_queue': orders_in_queue,
            'reviews': reviews,
            'showed_reviews': showed_reviews,
            'reviews_count': reviews.count(),
        }

        return render(request, self.template_name, context)

    

class EditServiceView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/edit_service.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().freelancer.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('service_view', kwargs={'pk': self.object.pk})


class DeleteServiceView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'services/confirm_delete.html'
    success_url = reverse_lazy('my_services')

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().freelancer.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class CreateReviewView(CreateView):
    model = Review
    fields = ['rating', 'comment']

    def form_valid(self, form):
        service = get_object_or_404(Service, pk=self.kwargs['pk'])
        form.instance.client = self.request.user.client
        form.instance.service = service
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('service_view', kwargs={'pk': self.object.service.pk})
    
class CreateOrderView(CreateView):
    model = Order
    fields = ['description']

    def form_valid(self, form):
        service = get_object_or_404(Service, pk=self.kwargs['pk'])
        form.instance.client = self.request.user.client
        form.instance.service = service
        form.instance.status = Order.Status.PENDING_APPROVAL
        form.instance.payment_method = 'Paypal'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('service_view', kwargs={'pk': self.object.service.pk})


class AllReviewsView(View):
    template_name = 'services/all_reviews.html'

    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        reviews = Review.objects.filter(service=service).order_by('-creation_date')

        for review in reviews:
            review.creation_date = review.creation_date.strftime('%b %d, %Y')

        context = {
            'service': service,
            'reviews': reviews,
        }
        return render(request, self.template_name, context)