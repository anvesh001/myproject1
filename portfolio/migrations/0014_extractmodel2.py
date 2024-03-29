# Generated by Django 2.0.7 on 2019-07-11 07:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20190711_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('requirements', models.CharField(choices=[('Register Your Business', 'Register Your Business'), ('simply your procces', 'simply your procces'), ('Tax Filling and Audit', 'Tax Filling and Audit'), ('Financial Services', 'Financial Services'), ('Get Trademark and File Patents', 'Get Trademark and File Patents'), ('Reports and Agreements', 'Reports and Agreements'), ('Closure & Changein Business', 'Closure & Changein Business'), ('Secretarial Compliances', 'Secretarial Compliances'), ('others', 'others')], default='Register Your Business', max_length=30)),
            ],
        ),
    ]
