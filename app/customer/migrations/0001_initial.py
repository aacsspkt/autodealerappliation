# Generated by Django 4.0 on 2022-01-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenship_no', models.CharField(max_length=50, unique=True, verbose_name='citizenship number')),
                ('pan_no', models.CharField(blank=True, default='None', max_length=50, verbose_name='pan number')),
                ('fullname', models.CharField(max_length=200, verbose_name='full name')),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, verbose_name='gender')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=20, verbose_name='phone number')),
                ('occupation', models.CharField(max_length=200, verbose_name='occupation')),
                ('city', models.CharField(max_length=200, verbose_name='town/city')),
                ('district', models.CharField(choices=[('Bhojpur', 'Bhojpur'), ('Dhankutca', 'Dhankuta'), ('Ilam', 'Ilam'), ('Jhapa', 'Jhapa'), ('Khotang', 'Khotang'), ('Morang', 'Morang'), ('Okhaldhunga', 'Okhaldhunga'), ('Panchthar', 'Panchthar'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Solukhumbu', 'Solukhumbu'), ('Sunsari', 'Sunsari'), ('Taplejung', 'Taplejung'), ('Terhathum', 'Terhathum'), ('Udayapur', 'Udayapur'), ('Bara', 'Bara'), ('Dhanusa', 'Dhanusa'), ('Mahotari', 'Mahottari'), ('Parsa', 'Parsa'), ('Rautahat', 'Rautahat'), ('Saptari', 'Saptari'), ('Sarlahi', 'Sarlahi'), ('Siraha', 'Siraha'), ('Bhaktapur', 'Bhaktapur'), ('Chitwan', 'Chitwan'), ('Dhading', 'Dhading'), ('Dolakha', 'Dolakha'), ('Kathmandu', 'Kathmandu'), ('Kavrepalanchok', 'Kavrepalanchok'), ('Lalitpur', 'Lalitpur'), ('Makawanpur', 'Makawanpur'), ('Nuwakot', 'Nuwakot'), ('Ramechhap', 'Ramechhap'), ('Rasuwa', 'Rasuwa'), ('Sindhuli', 'Sindhuli'), ('Sindhupalchowk', 'Sindhupalchok'), ('Baglung', 'Baglung'), ('Gorkha', 'Gorkha'), ('Kaski', 'Kaski'), ('Lamjung', 'Lamjung'), ('Manang', 'Manang'), ('Mustang', 'Mustang'), ('Myagdi', 'Myagdi'), ('Nawalpur', 'Nawalpur'), ('Parbat', 'Parbat'), ('Syandi', 'Syangja'), ('Tanahu', 'Tanahu'), ('Argakhanchi', 'Arghakhanchi'), ('Banke', 'Banke'), ('Bardiya', 'Bardiya'), ('Dang', 'Dang'), ('Gulmi', 'Gulmi'), ('Kapilvastu', 'Kapilvastu'), ('Parasi', 'Parasi'), ('Palpa', 'Palpa'), ('Pyuthan', 'Pyuthan'), ('Rolpa', 'Rolpa'), ('Rukum', 'Rukum'), ('Rupandehi', 'Rupandehi'), ('Dailekh', 'Dailekh'), ('Dolpa', 'Dolpa'), ('Humla', 'Humla'), ('Jajarkot', 'Jajarkot'), ('Jumla', 'Jumla'), ('Kalikot', 'Kalikot'), ('Mugu', 'Mugu'), ('Rukum Paschim', 'Rukum Paschim'), ('Salyan', 'Salyan'), ('Surkhet', 'Surkhet'), ('Achham', 'Achham'), ('Baitadi', 'Baitadi'), ('Bajhang', 'Bajhang'), ('Bajura', 'Bajura'), ('Dadeldhura', 'Dadeldhura'), ('Darchula', 'Darchula'), ('Doti', 'Doti'), ('Kailali', 'Kailali'), ('Kanchanpur', 'Kanchanpur')], max_length=40, verbose_name='district')),
                ('state', models.CharField(choices=[('Province No. 1', 'Province No 1'), ('Province No. 2', 'Province No 2'), ('Bagmati Province', 'Bagmati Province'), ('Gandaki Province', 'Gandaki Province'), ('Lumbini Province', 'Lumbini Province'), ('Karnali Province', 'Karnali Province'), ('Sudur-Paschim Province', 'Sudur Paschim Province')], max_length=40, verbose_name='state')),
                ('country', models.CharField(blank=True, default='Nepal', max_length=100, verbose_name='country')),
                ('address', models.TextField(max_length=500, verbose_name='address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
