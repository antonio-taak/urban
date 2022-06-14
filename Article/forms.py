from django import forms

from bootstrap_modal_forms.forms import BSModalModelForm
from ManagementSoftware.models import Article


class ArticleModelForm(BSModalModelForm):
    """
        Form per inserire i dati di un :class:`ManagementSoftware.models.Article`
    """

    class Meta:
        model = Article
        fields = ['name', 'measurement_unit', 'supplier_id']
        widgets = {
            'supplier_id': forms.Select(
                attrs={
                    'class': 'selectpicker',
                    'id': 'lsname',
                    'data-live-search': 'true'
                }
            ),
        }
