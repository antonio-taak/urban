from bootstrap_modal_forms.forms import BSModalModelForm
from ManagementSoftware.models import Client


class ClientModelForm(BSModalModelForm):
    """
        Form per inserire i dati di un :class:`ManagementSoftware.models.Client`
     """

    class Meta:
        model = Client
        fields = ['name']
