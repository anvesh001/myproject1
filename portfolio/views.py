from . import forms
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
from django.contrib.auth.models import User

def index(request):
     return render(request,'index.html')

class HomePageView(ListView):
        model = PortfolioModel
        template_name = 'index.html'
        paginate_by = 2
        queryset = PortfolioModel.objects.all()
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
'''
def index(request):
    user_list = ExtractModel2.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'users': users })
'''
