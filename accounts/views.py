from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from .models import Client, Freelancer
from django.contrib.auth.forms import AuthenticationForm


class SignupView(View):
    template_name = 'signup.html'


    def get(self, request):
        form = SignupForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_freelancer:
                Freelancer.objects.create(user=user)
                login(request, user)
                return redirect('freelancer_details')
            else:
                Client.objects.create(user=user)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
class LoginView(View):
    template_name = 'login.html'
    
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        error = None
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password'
        context = {
            'form': form,
            'error': error
        }
        return render(request, self.template_name, context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
class FreelancerDetailsView(LoginRequiredMixin, View):
    template_name = 'freelancer_details.html'

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'freelancer'):
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        freelancer = request.user.freelancer     
        experience = freelancer.experience
        portfolio = freelancer.portfolio if freelancer.portfolio else ''

        context = {
            'experience': experience,
            'portfolio': portfolio
        }
        
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        experience = request.POST.get('experience')
        portfolio = request.POST.get('portfolio')

        Freelancer.objects.filter(user=user).update(experience=experience, portfolio=portfolio)

        context = {
            'experience': experience,
            'portfolio': portfolio
        }

        return render(request, self.template_name, context)
