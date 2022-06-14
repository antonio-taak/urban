from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv

from .models import (
    Client,
    Site,
    Supplier,
    Article,
    Order,
)
from django.utils.decorators import method_decorator
from django.db.models import Q

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from django.views.generic import TemplateView


# Create your views here.
@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    """
        Mostra la homepage

        **Template:**
        `ManagementSoftware/home.html`
        """
    template_name = 'ManagementSoftware/home.html'


# CSV Download
def get_response(filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


def get_writer(response):
    return csv.writer(response)


@method_decorator(login_required, name='dispatch')
class DownloadArticlesCSV(TemplateView):
    """
        Scarica il CSV di :class:`ManagementSoftware.models.Article`.

        :ivar csv_name: Il nome che avrà il file una volta scaricato
    """
    csv_name = 'articoli.csv'

    def get(self, *args, **kwargs):
        response = get_response(self.csv_name)
        writer = get_writer(response)

        articles = Article.objects.all()
        writer.writerow(['Article name', 'supplier name', 'measurement_unit'])
        for article in articles:
            writer.writerow([article.name, article.supplier_id])
        return response


@method_decorator(login_required, name='dispatch')
class DownloadClientsCSV(TemplateView):
    """
            Scarica il CSV di :class:`ManagementSoftware.models.Client`.

            :ivar csv_name: Il nome che avrà il file una volta scaricato
        """
    csv_name = 'cliente.csv'

    def get(self, *args, **kwargs):
        response = get_response(self.csv_name)
        writer = get_writer(response)

        clients = Client.objects.all()
        writer.writerow(['clients name'])
        for client in clients:
            writer.writerow([client.name])
        return response


@method_decorator(login_required, name='dispatch')
class DownloadSitesCSV(TemplateView):
    """
            Scarica il CSV di :class:`ManagementSoftware.models.Site`.

            :ivar csv_name: Il nome che avrà il file una volta scaricato
        """
    csv_name = 'cantiere.csv'

    def get(self, *args, **kwargs):
        response = get_response(self.csv_name)
        writer = get_writer(response)

        sites = Site.objects.all()
        writer.writerow(['Sites name', 'client_id'])
        for site in sites:
            writer.writerow([site.name, site.client_id])
        return response


@method_decorator(login_required, name='dispatch')
class DownloadSuppliersCSV(TemplateView):
    """
            Scarica il CSV di :class:`ManagementSoftware.models.Supplier`.

            :ivar csv_name: Il nome che avrà il file una volta scaricato
        """
    csv_name = 'cantieri.csv'

    def get(self, *args, **kwargs):
        response = get_response(self.csv_name)
        writer = get_writer(response)

        suppliers = Supplier.objects.all()
        writer.writerow(['Supplie name'])
        for supplier in suppliers:
            writer.writerow([supplier.name])
        return response


@method_decorator(login_required, name='dispatch')
class DownloadOrdersCSV(TemplateView):
    """
            Scarica il CSV di :class:`ManagementSoftware.models.Order`.

            :ivar csv_name: Il nome che avrà il file una volta scaricato
            :ivar filter: Il filtro da appliccare a :class:`ManagementSoftware.Order` per prendere  dati da scaricare nel CSV
        """
    filter = ~Q(status="installed")
    csv_name = 'ordini.csv'

    def get(self, *args, **kwargs):
        response = get_response(self.csv_name)
        writer = get_writer(response)

        orders = Order.objects.filter(self.filter)
        writer.writerow(['article_id', 'suppliers', 'site_id', ' client', 'status', 'quantity', 'unita', 'date'])
        for order in orders:
            writer.writerow(
                [order.article_id, order.suppliers.name, order.site_id, order.clients.name, order.status,
                 order.quantity,
                 order.article_id.measurement_unit,
                 order.date]
            )
        return response


class TableView(TemplateView):
    """
        View generica per mostrare la tabella con i valori di tutti gli oggetti con possibilità di filtraggio

        :ivar model: Il model di cui vogliamo prendere tutti gli oggetti (o filtrare)
        :ivar template_name: Il template da visualizzare sul frontend
        :ivar model_filter: Il filtro da applicare per prendere i dati, di default prende tutti i dati del model
        :ivar context_object_name: Il nome della chiave relativo a tutti i dati nel model nel context (quello che si userà nel template)
        :ivar order_by: Order the results by this column

        **Template:** `Dinamico, dipende da template_name`
    """
    model = None
    template_name = None
    model_filter = Q(pk__isnull=False)
    context_object_name = None

    def get(self, *args, **kwargs):
        objects = self.model.objects.filter(self.model_filter)
        context = {self.context_object_name: objects}

        return render(self.request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class CreateView(BSModalCreateView):
    """
        View generica per mostrare il form di inserimento e creare l'oggetto di un model

        :ivar model: Il model di cui vogliamo prendere tutti gli oggetti (o filtrare)
        :ivar context_object_name: Il nome della chiave relativo a tutti i dati nel model nel context (quello che si userà nel template)
        :ivar template_name: Il template da visualizzare sul frontend
        :ivar form_class: La classe del form da visualizzare sul frontend
        :ivar success_url: L'url su cui andare in caso di successo

        **Template:** `Dinamico, dipende da template_name`
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UpdateView(BSModalUpdateView):
    """
        View generica per mostrare il form di aggiornamento e aggiornare l'oggetto di un model

        :ivar model: Il model di cui vogliamo prendere tutti gli oggetti (o filtrare)
        :ivar template_name: Il template da visualizzare sul frontend
        :ivar form_class: La classe del form da visualizzare sul frontend
        :ivar success_url: L'url su cui andare in caso di successo

        **Template:** `Dinamico, dipende da template_name`
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class DeleteView(BSModalDeleteView):
    """
        View generica per eliminare un oggetto di un model

        :ivar model: Il model di cui vogliamo prendere tutti gli oggetti (o filtrare)
        :ivar template_name: Il template da visualizzare sul frontend
        :ivar success_url: L'url su cui andare in caso di successo
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
