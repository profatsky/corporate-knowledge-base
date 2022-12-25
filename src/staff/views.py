from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from staff.models import Employee


class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'staff/profile.html'
    model = Employee
    login_url = 'login'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.pk)


class StaffView(LoginRequiredMixin, generic.ListView):
    template_name = 'staff/staff.html'
    model = Employee
    login_url = 'login'
