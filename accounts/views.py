from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm
from django.contrib.auth import login, logout
from .models import Client, Freelancer
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
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
                """ If the user is a freelancer, redirect them to the freelancer_signup page. THIS IS NOT IMPLEMENTED YET. """
                return redirect('freelancer_signup')
            else:
                Client.objects.create(user=user)
            login(request, form.instance)
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
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print("INVALID")
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