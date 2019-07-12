from django.contrib import admin

# Register your models here.
from .models import PortfolioModel,ExtractModel2
admin.site.register(PortfolioModel)
#admin.site.register(ExtractModel)
admin.site.register(ExtractModel2)
