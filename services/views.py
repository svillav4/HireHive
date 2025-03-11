from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from .forms import ServiceForm
from .models import Service
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class MyServicesView(View):
    template_name = 'services/my_services.html'

    def get(self, request,):
        services = Service.objects.all()
        return render(request, self.template_name, {"services": services})


class CreateServiceView(LoginRequiredMixin, TemplateView):
    template_name = 'services/create_service.html'

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return HttpResponse("No tienes permisos para crear un servicio.", status=403)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = ServiceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            freelancer = request.user.freelancer
            service = form.save(commit=False)
            service.freelancer = freelancer
            service.save()
            return redirect('service_success')
        
        return render(request, self.template_name, {'form': form})

class ServiceSuccessView(TemplateView):
    template_name = 'products/success.html'
