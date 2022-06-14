from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    """
        Salva un cliente

         :ivar name: Il nome del cliente
    """
    name = models.CharField(max_length=200, verbose_name="Nome del cliente")

    class Meta:
        verbose_name = 'client'
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class Site(models.Model):
    """
            Salva un cantiere

            :ivar name: Il nome del cantiere
            :ivar client_id: Il cliente che ha richiesto la costruzione nel cantiere
    """
    name = models.CharField(max_length=200, verbose_name="Nome del cantiere")
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Nome del cliente")

    class Meta:
        verbose_name = 'site'
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class Supplier(models.Model):
    """
            Salva un fornitore

            :ivar name: Il nome del fonitore
    """
    name = models.CharField(max_length=200, verbose_name="Nome del fornitore")

    class Meta:
        verbose_name = 'supplier'
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    """
            Salva un articolo

            :ivar name: Il nome dell'articolo
            :ivar supplier_id: Il fornitore da cui si acquista l'articolo
            :ivar measurement_unit: L'unità di misura con cui misurare l'articolo nell'ordine (:class:`ManagementSoftware.models.Order`)
    """
    name = models.CharField(max_length=200, verbose_name="Nome dell'articolo")
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Nome del fornitore")
    measurement_unit = models.CharField(max_length=50, verbose_name="Unità di misura", default="")

    class Meta:
        verbose_name = 'article'
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


STATUS_CHOICES = (
    ('installed', 'Installato'),
    ('delivered', 'Consegnato'),
    ('in-stock', 'In Giacenza'),
    ('ordered', 'Ordinato'),
    ('withdraw', 'Da Ritirare'),
    ('to-confirm', 'In Attesa'),
    ('to-order', 'Da Ordinare'),
)


class Order(models.Model):
    """
            Salva un ordine

            :ivar date: La data in cui è stato effettuato l'ordine
            :ivar status: Lo stato dell'ordine
            :ivar quantity: La quantità ordinata dell'ordine (l'unità di misura è rappresentata in :class:`ManagementSoftware.models.Article`
            :ivar article_id: L'articolo a cui si riferisce l'ordine
            :ivar site_id: Il cantiere a cui si riferisce l'ordine
            :ivar suppliers: Il fornitore (SOLO PER IL FORM)
            :ivar clients: Il cliente (SOLO PER IL FORM)
    """
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Stato dell ordine")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantità dell ordine")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Nome dell articolo")
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name="Nome del cantiere")
    suppliers = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Nome dell Fornitori")
    clients = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Nome dell Clienti")

    class Meta:
        verbose_name = 'order'
        ordering = ("article_id__supplier_id__name",)

    def __str__(self):
        return str(self.status)
