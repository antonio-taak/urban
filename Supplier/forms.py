from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from ManagementSoftware.models import Supplier


class SupplierModelForm(BSModalModelForm):
    """
        Form per inserire o aggiornare i dati di un :class:`ManagementSoftware.models.Supplier`
    """
    class Meta:
        model = Supplier
        fields = ['name']
