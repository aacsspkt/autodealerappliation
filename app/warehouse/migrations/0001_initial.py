# Generated by Django 4.0 on 2022-01-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Dim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.BigIntegerField(verbose_name='Customer Id')),
                ('citizenship_no', models.CharField(max_length=50, verbose_name='Citizenship Number')),
                ('pan_no', models.CharField(max_length=50, verbose_name='PAN Number')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=200, verbose_name='Middle Name')),
                ('surname', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Record_Dim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.BigIntegerField(verbose_name='Purchase Id')),
                ('invoice_no', models.CharField(max_length=50, verbose_name='Invoice Number')),
                ('vendor_name', models.CharField(max_length=200, verbose_name='Vendor Name')),
                ('vendor_address', models.CharField(max_length=300, verbose_name='Vendor Address')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Purchase Amount')),
                ('sale_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sale Amount')),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('finance_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Finance Amount')),
                ('exchange_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Exchange Amount')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_Record_Dim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_id', models.BigIntegerField(verbose_name='Sale Id')),
                ('invoice_no', models.CharField(blank=True, default='None', max_length=50, verbose_name='Invoice Number')),
                ('dc_no', models.CharField(blank=True, default='None', max_length=50, verbose_name='Delivery Challan No.')),
                ('payment_mode', models.CharField(blank=True, default='None', max_length=50, verbose_name='Payment Mode')),
            ],
        ),
        migrations.CreateModel(
            name='Scheme_Dim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_id', models.BigIntegerField(verbose_name='Scheme Id')),
                ('scheme_name', models.CharField(max_length=300, verbose_name='Scheme Name')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Time_Dim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField()),
                ('day', models.PositiveSmallIntegerField()),
                ('day_of_week', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Dim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.BigIntegerField(verbose_name='Vehicle Id')),
                ('vehicle_model', models.CharField(max_length=100, verbose_name='Vehicle Model')),
                ('color', models.CharField(max_length=100)),
                ('chasis_no', models.CharField(max_length=100, verbose_name='Chasis Number')),
                ('engine_no', models.CharField(max_length=100, verbose_name='Engine Number')),
                ('reg_no', models.CharField(max_length=100, verbose_name='Registration Number')),
                ('key_no', models.CharField(max_length=20, verbose_name='Key Number')),
                ('battery_no', models.CharField(max_length=100, verbose_name='Battery Number')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Purchase Price')),
            ],
        ),
        migrations.AddConstraint(
            model_name='vehicle_dim',
            constraint=models.UniqueConstraint(fields=('chasis_no', 'engine_no'), name='UniqueChasisEngine'),
        ),
        migrations.AddConstraint(
            model_name='vehicle_dim',
            constraint=models.UniqueConstraint(fields=('reg_no',), name='UniqueVehicleRegistration'),
        ),
        migrations.AddConstraint(
            model_name='vehicle_dim',
            constraint=models.UniqueConstraint(fields=('vehicle_id',), name='UniqueVehicleId'),
        ),
        migrations.AddConstraint(
            model_name='scheme_dim',
            constraint=models.UniqueConstraint(fields=('scheme_id',), name='UniqueSchemeId'),
        ),
        migrations.AddConstraint(
            model_name='sale_record_dim',
            constraint=models.UniqueConstraint(fields=('sale_id',), name='UniqueSaleId'),
        ),
        migrations.AddField(
            model_name='sale_fact',
            name='customer_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='warehouse.customer_dim'),
        ),
        migrations.AddField(
            model_name='sale_fact',
            name='purchase_record_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='warehouse.purchase_record_dim'),
        ),
        migrations.AddField(
            model_name='sale_fact',
            name='sale_record_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='warehouse.sale_record_dim'),
        ),
        migrations.AddField(
            model_name='sale_fact',
            name='scheme_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='warehouse.scheme_dim'),
        ),
        migrations.AddField(
            model_name='sale_fact',
            name='time_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='warehouse.time_dim'),
        ),
        migrations.AddField(
            model_name='sale_fact',
            name='vehicle_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='warehouse.vehicle_dim'),
        ),
        migrations.AddConstraint(
            model_name='purchase_record_dim',
            constraint=models.UniqueConstraint(fields=('purchase_id',), name='UniquePurchaseId'),
        ),
        migrations.AddConstraint(
            model_name='customer_dim',
            constraint=models.UniqueConstraint(fields=('citizenship_no',), name='UniqueCitizenship'),
        ),
        migrations.AddConstraint(
            model_name='customer_dim',
            constraint=models.UniqueConstraint(fields=('pan_no',), name='UniquePAN'),
        ),
    ]
