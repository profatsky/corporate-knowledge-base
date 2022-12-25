from django.contrib.auth import views
from django.urls import reverse_lazy

from .forms import LoginForm


class UserLoginView(views.LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


class UserLogoutView(views.LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')
