from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class  PortfolioModel(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images/')
    qualification=models.CharField(max_length=255, default='')
    experince=models.PositiveSmallIntegerField(choices=list(zip(range(1, 10), range(1, 10))), default=0)
    keywords=models.CharField(max_length=255,default='')
    area_of_expertise=models.TextField(default='')
    price=models.PositiveSmallIntegerField(default=0)
    country = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.name
class ExtractModel(models.Model):
            status_choices=[
            ('Register Your Business','Register Your Business'),
            ('simply your procces','simply your procces'),
            ('Tax Filling and Audit','Tax Filling and Audit'),
            ('Financial Services','Financial Services'),
            ('Get Trademark and File Patents','Get Trademark and File Patents'),
            ('Reports and Agreements','Reports and Agreements'),
            ('Closure & Changein Business','Closure & Changein Business'),
            ('Secretarial Compliances','Secretarial Compliances'),
            ('others','others'),
            ]

            cname=models.CharField(max_length= 200,null = True)
            email=models.EmailField(null = True)
            phone = PhoneNumberField()
            requirements=models.CharField(max_length=30,null = True)

            def __str__(self):
                return self.cname

class ExtractModel2(models.Model):
            STATUS_CHOICES=[
            ('Register Your Business','Register Your Business'),
            ('simply your procces','simply your procces'),
            ('Tax Filling and Audit','Tax Filling and Audit'),
            ('Financial Services','Financial Services'),
            ('Get Trademark and File Patents','Get Trademark and File Patents'),
            ('Reports and Agreements','Reports and Agreements'),
            ('Closure & Changein Business','Closure & Changein Business'),
            ('Secretarial Compliances','Secretarial Compliances'),
            ('others','others')
            ]
            cname=models.CharField(max_length= 200)
            email=models.EmailField()
            phone = PhoneNumberField()
            requirements=models.CharField(max_length=30,choices=STATUS_CHOICES, default='Register Your Business')
