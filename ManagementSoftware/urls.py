from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.db.models import Q

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # Authentication views
    path(
        'account/login/',
        view=auth_views.LoginView.as_view(template_name='ManagementSoftware/login.html', authentication_form=LoginForm),
        name='login'
    ),
    path('account/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Download CSV views
    path('article-csv/', views.DownloadArticlesCSV.as_view(), name='article_csv'),
    path('client-csv/', views.DownloadClientsCSV.as_view(), name='client_csv'),
    path('site-csv/', views.DownloadSitesCSV.as_view(), name='site_csv'),
    path('supplier-csv/', views.DownloadSuppliersCSV.as_view(), name='supplier_csv'),
    path('order-csv/', views.DownloadOrdersCSV.as_view(), name='order_csv'),
    path(
        'archiveorder-csv/',
        view=views.DownloadOrdersCSV.as_view(filter=Q(status="installed"), csv_name="ordini_archiviati.csv"),
        name='archiveorder_csv'
    ),
]
