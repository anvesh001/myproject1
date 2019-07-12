"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolio.views import HomePageView
from portfolio import views
from django.conf.urls import include, url
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('/home/',views.index),
    path('home/',views.home, name='home'),
    path('index/',HomePageView.as_view()),
    path('showform/',views.showform, name='showform'),
]
'''
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    #path('/home/',views.index),
    url(r'^home/$',views.home, name='home'),
    url(r'index/$',HomePageView.as_view()),
    url(r'showform/$',views.showform, name='showform'),
    url(r'^index/(?P<page>[a-z0-9]+)/$',HomePageView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
