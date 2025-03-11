from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from .forms import ServiceForm
from .models import Service
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ShowServiceView(View):
    template_name = 'services/show_services.html'

    def get(self, request,):
        services = Service.objects.all()
        return render(request, self.template_name, {"services": services})


class CreateServiceView(TemplateView):
    template_name = 'services/create_service.html'

    # @login_required
    def get(self, request, *args, **kargs):
        #if not request.user.is_freelancer:  # Validación con el booleano
            #return HttpResponse("No tienes permisos para crear un servicio.", status=403)
        
        form = ServiceForm()
        return render(request, self.template_name, {'form' : form})
    
    # @login_required
    def post(self, request, *args, **kwargs):
        #if not request.user.is_freelancer:  # Validación con el booleano
            #return HttpResponse("No tienes permisos para crear un servicio.", status=403)
         
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            #service.freelancer = Freelancer.objects.get(user=request.user)
            service.save()
            return redirect('service_success')
        return render(request, self.template_name, {'form': form})

class ServiceSuccessView(TemplateView):
    template_name = 'products/success.html'
