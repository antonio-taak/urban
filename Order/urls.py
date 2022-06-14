from django.urls import path

from ManagementSoftware.models import Order
from . import views

from django.urls import reverse_lazy
from django.db.models import Q
from ManagementSoftware import views as generic_views
from .forms import OrderModelForm, OrderUpdateModelForm

urlpatterns = [
    path('ordini/', generic_views.TableView.as_view(
        model=Order,
        template_name='order/order_list.html',
        context_object_name="orders",
        model_filter=~Q(status="installed")
    ), name='orders'),
    path('ordini/raggruppati', views.GroupOrder.as_view(is_archive=False), name='grouped_orders'),
    path('ordini/crea/', generic_views.CreateView.as_view(
        model=Order,
        context_object_name="orders",
        template_name='order/order_create.html',
        form_class=OrderModelForm,
        success_url=reverse_lazy('orders'),
    ), name='order_create'),
    path('ordini/aggiorna/<int:pk>', generic_views.UpdateView.as_view(
        model=Order,
        template_name='order/order_update.html',
        form_class=OrderUpdateModelForm,
        success_url=reverse_lazy('orders')
    ), name='order_update'),
    path('ordini/elimina/<int:pk>', generic_views.DeleteView.as_view(
        model=Order,
        template_name='order/order_delete.html',
        success_url=reverse_lazy('orders')
    ), name='order_delete'),
    path('ordini/archiviati', generic_views.TableView.as_view(
        model=Order,
        template_name='order/archiveorder_list.html',
        context_object_name="orders",
        model_filter=Q(status="installed")
    ), name='archiveorders'),
    path('ordini/archiviati/raggruppati', views.GroupOrder.as_view(is_archive=True), name='grouped_archived_orders'),
    path('ordini/archiviati/aggiorna/<int:pk>', generic_views.UpdateView.as_view(
        model=Order,
        template_name='order/order_update.html',
        form_class=OrderUpdateModelForm,
        success_url=reverse_lazy('archiveorders')
    ), name='archiveorder_update'),
    path('ordini/archiviati/elimina/<int:pk>', generic_views.DeleteView.as_view(
        model=Order,
        template_name='order/order_delete.html',
        success_url=reverse_lazy('archiveorders')
    ), name='archiveorder_delete'),
    path('ajax/load-sites/', views.LoadSites.as_view(), name='ajax_load_sites'),
    path('ajax/load-suppliers/', views.LoadSuppliers.as_view(), name='ajax_load_suppliers'),
    path('ordini/json/', views.AllOrders.as_view(), name='orders_json'),

]
