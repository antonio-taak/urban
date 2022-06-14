from django.urls import path

from ManagementSoftware.models import Supplier
from . import views
from ManagementSoftware import views as generic_views
from django.urls import reverse_lazy
from .forms import SupplierModelForm


urlpatterns = [
    path('fornitori/', generic_views.TableView.as_view(
        model=Supplier,
        template_name='supplier/supplier_list.html',
        context_object_name="suppliers"
    ), name='suppliers'),
    path('fornitori/crea/', generic_views.CreateView.as_view(
        model=Supplier,
        context_object_name="suppliers",
        template_name='supplier/supplier_create.html',
        form_class=SupplierModelForm,
        success_url=reverse_lazy('suppliers'),
    ), name='supplier_create'),
    path('fornitori/aggiorna/<int:pk>', generic_views.UpdateView.as_view(
        model=Supplier,
        template_name='supplier/supplier_update.html',
        form_class=SupplierModelForm,
        success_url=reverse_lazy('suppliers')
    ), name='supplier_update'),
    path('fornitori/elimina/<int:pk>', generic_views.DeleteView.as_view(
        model=Supplier,
        template_name='supplier/supplier_delete.html',
        success_url=reverse_lazy('suppliers')
    ), name='supplier_delete'),
    path('fornitori/json/', views.AllSuppliers.as_view(), name='suppliers_json'),
]