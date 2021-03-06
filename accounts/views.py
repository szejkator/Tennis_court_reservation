from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views


class RegisterUserForm(CreateView):
    model = User
    template_name = 'user_reg_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("reservations_urls:login_main")


class PasswordReset():
    pass


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy("reservations_urls:login_main")
