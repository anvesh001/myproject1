# Generated by Django 2.0.7 on 2019-07-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_extractmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractmodel',
            name='requirements',
            field=models.CharField(choices=[('Register Your Business', 'Register Your Business'), ('simply your procces', 'simply your procces'), ('Tax Filling and Audit', 'Tax Filling and Audit'), ('Financial Services', 'Financial Services'), ('Get Trademark and File Patents', 'Get Trademark and File Patents'), ('Reports and Agreements', 'Reports and Agreements'), ('Closure & Changein Business', 'Closure & Changein Business'), ('Secretarial Compliances', 'Secretarial Compliances'), ('others', 'others')], default='Register Your Business', max_length=30),
        ),
    ]