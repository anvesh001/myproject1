# Generated by Django 2.0.7 on 2019-07-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20190711_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractmodel2',
            name='requirements',
            field=models.CharField(choices=[('Register Your Business', 'Register Your Business'), ('simply your procces', 'simply your procces'), ('Tax Filling and Audit', 'Tax Filling and Audit'), ('Financial Services', 'Financial Services'), ('Get Trademark and File Patents', 'Get Trademark and File Patents'), ('Reports and Agreements', 'Reports and Agreements'), ('Closure & Changein Business', 'Closure & Changein Business'), ('Secretarial Compliances', 'Secretarial Compliances'), ('others', 'others')], default='Register Your Business', max_length=30),
        ),
    ]
