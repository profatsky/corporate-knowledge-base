from django.urls import path

from .views import CatalogListView, DocumentListView, index

urlpatterns = [
    path('', index, name='index'),
    path('catalogs/', CatalogListView.as_view(), name='catalogs'),
    path('catalogs/<int:catalog_pk>', DocumentListView.as_view(), name='documents'),
]
