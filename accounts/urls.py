from django.urls import path
from .views import SignUpView, login,register, dashboard, logout



urlpatterns = [
      path('login/', login, name='login'),
      path('register/', register, name='register'),
      path('dashboard/', dashboard, name='dashboard'),
      path('logout/', logout, name="logout"),
      path('signup/', SignUpView.as_view(), name='signup')
     

]