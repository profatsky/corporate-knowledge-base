from django.urls import path

from .views import EmployeeDetailView, EmployeeListView

urlpatterns = [
    path('staff/', EmployeeListView.as_view(), name='staff'),
    path('staff/<int:pk>/', EmployeeDetailView.as_view(), name='profile'),
]
