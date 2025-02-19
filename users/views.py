import secrets
from users.models import User
from users.forms import UserRegisterForm#
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from config import settings
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_register.html'
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token=token
        user.save()
        host=self.request.get_host()
        url=f'http://{host}/users/email-confirm/{token}/'
        send_mail(

            subject = 'Подтверждение',
            message = f'Привет! Перейли по ссылке {url}',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
       user = get_object_or_404(User, token=token)
       user.is_active = True
       user.save()
       return redirect(reverse('users:login'))

