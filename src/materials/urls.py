from django.urls import path

from .views import CatalogListView, DocumentListView

urlpatterns = [
    path('catalogs/', CatalogListView.as_view(), name='catalogs'),
    path('catalogs/<int:catalog_pk>', DocumentListView.as_view(), name='documents'),
]
