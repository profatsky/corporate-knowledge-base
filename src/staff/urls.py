from django.urls import path

from .views import ProfileView, StaffView

urlpatterns = [
    path('staff/', StaffView.as_view(), name='staff'),
    path('staff/<int:pk>/', ProfileView.as_view(), name='profile'),
]
