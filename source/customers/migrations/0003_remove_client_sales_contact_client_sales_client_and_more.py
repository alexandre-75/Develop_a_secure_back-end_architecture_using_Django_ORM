# Generated by Django 4.2 on 2023-04-22 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_alter_client_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='sales_contact',
        ),
        migrations.AddField(
            model_name='client',
            name='sales_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='status_client',
            field=models.CharField(choices=[('POTENTIAL', 'POTENTIAL'), ('EXISTING', 'EXISTING')], default='', max_length=64),
            preserve_default=False,
        ),
    ]
