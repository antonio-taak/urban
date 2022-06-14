from django.urls import path

from . import views
from ManagementSoftware import views as generic_views
from django.urls import reverse_lazy
from ManagementSoftware.models import Client
from .forms import ClientModelForm


urlpatterns = [
    path('clienti/', generic_views.TableView.as_view(
        model=Client,
        template_name='client/client_list.html',
        context_object_name="clients"
    ), name='clients'),
    path('clienti/crea/', generic_views.CreateView.as_view(
        model=Client,
        context_object_name="clients",
        template_name='client/client_create.html',
        form_class=ClientModelForm,
        success_url=reverse_lazy('clients'),
    ), name='client_create'),
    path('clienti/aggiorna/<int:pk>', generic_views.UpdateView.as_view(
        model=Client,
        template_name='client/client_update.html',
        form_class=ClientModelForm,
        success_url=reverse_lazy('clients')
    ), name='client_update'),
    path('clienti/elimina/<int:pk>', generic_views.DeleteView.as_view(
        model=Client,
        template_name='client/client_delete.html',
        success_url=reverse_lazy('clients')
    ), name='client_delete'),
    path('clienti/json/', views.allclients, name='clients_json'),
]