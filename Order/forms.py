from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from ManagementSoftware.models import (
    Client,
    Site,
    Supplier,
    Article,
    Order,
)


class OrderModelForm(BSModalModelForm):
    """
        Form per inserire i dati di un :class:`ManagementSoftware.models.Order`
     """

    class Meta:
        model = Order
        fields = ['clients', 'site_id', 'suppliers', 'article_id', 'quantity', 'status']
        widgets = {
            'clients': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lclients',
                'data-live-search': 'true'
            }),
            'site_id': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lsites',
                'data-live-search': 'true'
            }),
            'suppliers': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lsuppliers',
                'data-live-search': 'true'
            }),
            'article_id': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'larticles',
                'data-live-search': 'true'
            }),
            'status': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lstatus',
                'data-live-search': 'true'
            }),
        }


class OrderUpdateModelForm(BSModalModelForm):
    """
        Form per aggiornare i dati di un :class:`ManagementSoftware.models.Order`
     """

    class Meta:
        model = Order
        fields = ['clients', 'site_id', 'suppliers', 'article_id', 'quantity', 'status']
        widgets = {
            'clients': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lclients',
                'data-live-search': 'true'
            }),
            'site_id': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lsites',
                'data-live-search': 'true'
            }),
            'suppliers': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lsuppliers',
                'data-live-search': 'true'
            }),
            'article_id': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'larticles',
                'data-live-search': 'true'
            }),
            'status': forms.Select(attrs={
                'class': 'selectpicker',
                'id': 'lstatus',
                'data-live-search': 'true'
            }),
        }
