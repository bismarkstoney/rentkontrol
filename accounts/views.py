from django.shortcuts import render
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from .forms import CustomUserCreationForm


def register(request):
    return render (request, 'account/register.html')
def login(request):
    return render(request, 'account/login.html')
def dashboard(request):
    return render (request, 'account/dashbaord.html')

def logout(request):
    return redirect ('index')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'account/signup.html'

# # class LoginUpView(View):
# #     form_class = LoginUserForm
# #     success_url = reverse_lazy('index')
# #     template_name = 'account/login.html'

