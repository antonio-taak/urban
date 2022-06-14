# Generated by Django 4.0.3 on 2022-06-08 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementSoftware', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Setting',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('name',), 'verbose_name': 'article'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',), 'verbose_name': 'client'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('article_id__supplier_id__name',), 'verbose_name': 'order'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ('name',), 'verbose_name': 'site'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ('name',), 'verbose_name': 'supplier'},
        ),
    ]