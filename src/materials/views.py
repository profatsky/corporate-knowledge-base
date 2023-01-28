from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.views import generic

from .models import Catalog, Document


def index(request):
    return redirect('catalogs')


class CatalogListView(LoginRequiredMixin, generic.ListView):
    template_name = 'materials/catalogs.html'
    model = Catalog
    login_url = 'login'

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        return self.model.objects.filter(
            document__is_private__lte=self.request.user.employee.extended_access
        ).distinct()


class DocumentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'materials/documents.html'
    model = Document
    login_url = 'login'

    def get_queryset(self):
        catalog = Catalog.objects.get(pk=self.kwargs.get('catalog_pk'))
        if not catalog:
            raise Http404
        documents = self.model.objects.filter(catalog__pk=catalog.pk)
        if not self.request.user.is_staff:
            documents = documents.filter(is_private__lte=self.request.user.employee.extended_access)
            if not documents:
                raise Http404
        doc_viewer_path = 'https://docs.yandex.ru/docs/view?url='
        for document in documents:
            document.view_path = doc_viewer_path + self.request.build_absolute_uri(document.disk_path.url)
        return documents
