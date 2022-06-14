from django.urls import path

from ManagementSoftware.models import Site
from . import views
from ManagementSoftware import views as generic_views
from django.urls import reverse_lazy
from .forms import SiteModelForm


urlpatterns = [
    path('cantieri/', generic_views.TableView.as_view(
        model=Site,
        template_name='site/site_list.html',
        context_object_name="sites"
    ), name='sites'),
    path('cantieri/crea/', generic_views.CreateView.as_view(
        model=Site,
        context_object_name="sites",
        template_name='site/site_create.html',
        form_class=SiteModelForm,
        success_url=reverse_lazy('sites'),
    ), name='site_create'),
    path('cantieri/aggiorna/<int:pk>', generic_views.UpdateView.as_view(
        model=Site,
        template_name='site/site_update.html',
        form_class=SiteModelForm,
        success_url=reverse_lazy('sites')
    ), name='site_update'),
    path('cantieri/elimina/<int:pk>', generic_views.DeleteView.as_view(
        model=Site,
        template_name='site/site_delete.html',
        success_url=reverse_lazy('sites')
    ), name='site_delete'),
    path('cantieri/json/', views.AllSites.as_view(), name='sites_json'),
]