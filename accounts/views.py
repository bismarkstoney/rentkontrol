from django.shortcuts import render
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views  import SuccessMessageMixin
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from  contacts.models import Contacts 


def register(request):
    return render (request, 'account/register.html')
def login(request):
    return render(request, 'account/login.html')
def dashboard(request):
    user_contacts=Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts': user_contacts
    }
    return render (request, 'account/dashboard.html',context)

def logout(request):
    return redirect ('index')

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'
    success_message= "Account was created successfully"

# # class LoginUpView(View):
# #     form_class = LoginUserForm
# #     success_url = reverse_lazy('index')
# #     template_name = 'account/login.html'

