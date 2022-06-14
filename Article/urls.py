from django.urls import path

from ManagementSoftware.models import Article
from . import views
from ManagementSoftware import views as generic_views
from .forms import ArticleModelForm
from django.urls import reverse_lazy

urlpatterns = [
    path('articoli/', generic_views.TableView.as_view(
        model=Article,
        template_name='article/article_list.html',
        context_object_name="articles"
    ), name='articles'),
    path('articoli/crea/', generic_views.CreateView.as_view(
        model=Article,
        context_object_name="articles",
        template_name='article/article_create.html',
        form_class=ArticleModelForm,
        success_url=reverse_lazy('articles'),
    ), name='article_create'),
    path('articoli/aggiorna/<int:pk>', generic_views.UpdateView.as_view(
        model=Article,
        template_name='article/article_update.html',
        form_class=ArticleModelForm,
        success_url=reverse_lazy('articles')
    ), name='article_update'),
    path('articoli/elimina/<int:pk>', generic_views.DeleteView.as_view(
        model=Article,
        template_name='article/article_delete.html',
        success_url=reverse_lazy('articles')
    ), name='article_delete'),
    path('articoli/json/', views.all_articles, name='articles_json'),
]
