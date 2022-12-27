from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from staff.models import Employee


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'staff/profile.html'
    model = Employee
    login_url = 'login'

    def get_object(self, **kwargs):
        return self.model.objects.get(user=self.kwargs.get('pk'))


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'staff/staff.html'
    model = Employee
    login_url = 'login'
