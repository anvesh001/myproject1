from . import forms
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.shortcuts import render
from .models import ExtractModel2
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import PortfolioModel,ExtractModel
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ExtractForm,ExtractForm2

def index(request):
     return render(request,'index.html')

class HomePageView(ListView):
        model = PortfolioModel
        template_name = 'index.html'
'''
def home(request):
    if request.method == 'POST':
        form = ExtractForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            return render(request,'index.html')

    else:
        form = ExtractForm()
    return render(request, 'view_all.html', {'form': form})
'''

def home(request):
        print('hello submitted')
        cname=request.POST.get('cname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        requirements=request.POST.get('requirements')
        print(cname,email,phone,requirements)
        contactmodel=ExtractModel(cname=cname,email=email,phone=phone,requirements=requirements)
        contactmodel.save()

        return render(request,'view_all1.html',{})

def showform(request):
    form = forms.ExtractForm2(request.POST)
    if request.method == 'POST':
        form = ExtractForm2(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')

    return render(request, 'view_all.html', {
        'form': form
    })
