from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .forms import ServiceForm
from .models import Service
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
class SearchBarView(TemplateView):
    template_name = 'pages/home.html'
    
    def get(self, request):
        search = request.GET.get('search', '')
        services = Service.objects.filter(Q(title__icontains=search) | Q(description__icontains=search)).distinct()
        return render(request, self.template_name, {"services": services})


class MyServicesView(LoginRequiredMixin, View):
    template_name = 'services/my_services.html'

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        services = Service.objects.all()
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
        service = Service.objects.get(id=id)
        return render(request, self.template_name, {'service': service})
