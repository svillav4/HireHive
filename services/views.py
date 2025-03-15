from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .forms import ServiceForm
from .models import Service
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get(self, request):
        search = request.GET.get('search', '').strip()  # Get search query

        # Filter services by search query
        if search:
            services = Service.objects.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            ).distinct()
        else:
            services = Service.objects.all()

        # Filter services by price range
        filtered = request.GET.get('filter')
        if filtered == 'basic':
            services = services.filter(price__lte=100)
        elif filtered == 'midrange':
            services = services.filter(price__gte=100, price__lte=400)
        elif filtered == 'highend':
            services = services.filter(price__gte=400)

        context = {
            'services': services,
            'search': search,
            'filtered': filtered,
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


class CreateServiceView(LoginRequiredMixin, TemplateView):
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
            freelancer = request.user.freelancer
            service = form.save(commit=False)
            service.freelancer = freelancer
            service.save()
            return redirect('success')
        
        return render(request, self.template_name, {'form': form})


class ServiceSuccessView(TemplateView):
    template_name = 'services/success.html'


class ServiceView(LoginRequiredMixin, View):
    template_name = 'services/service_view.html'

    def get(self, request, id):
        service = get_object_or_404(Service, id=id)
        return render(request, self.template_name, {'service': service})
