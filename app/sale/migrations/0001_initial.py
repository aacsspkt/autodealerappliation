# Generated by Django 4.0 on 2022-01-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('vehicle', '0001_initial'),
        ('scheme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=50, unique=True, verbose_name='invoice number')),
                ('challan_no', models.CharField(max_length=50, verbose_name='challan number')),
                ('sale_date', models.DateField(verbose_name='sale date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='amount')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='discount')),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('E-Banking', 'E Banking'), ('Cash and Cheque', 'Cash Cheque'), ('Cash and E-Banking', 'Cash E Banking'), ('Cheque and E-Banking', 'Cheque E Banking'), ('Cash, Cheque and E-Banking', 'Cash Cheque E Banking')], max_length=50, verbose_name='payment mode')),
                ('finance_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='finance amount')),
                ('exchange_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='exchange amount')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='customer')),
                ('scheme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheme.scheme', verbose_name='scheme')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle', verbose_name='vehicle')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
    ]