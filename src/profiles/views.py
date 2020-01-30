from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
class SignInView(LoginView):
    template_name = 'profiles/signin.html'
    success_url = reverse_lazy('homepage')

class RegisterUserView(SuccessMessageMixin,FormView):
    form_class = UserCreationForm
    template_name = 'profiles/register.html'
    success_url = reverse_lazy('profiles:signin')
    success_message = 'Başarı ile kayıt oldunuz. U shall not pass unless u sign in'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)