from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from ManagementSoftware.models import Site


class SiteModelForm(BSModalModelForm):
    """
        Form per inserire o aggiornare i dati di un :class:`ManagementSoftware.models.Site`
     """
    class Meta:
        model = Site
        fields = ['name', 'client_id']
        widgets = {
            'client_id': forms.Select(
                attrs={
                    'class': 'selectpicker',
                    'id': 'lclname',
                    'data-live-search': 'true'
                }
            ),
        }
