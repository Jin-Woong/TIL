"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pages import views  # views에 매핑시켜주기 위한 import

urlpatterns = [
    path('template_language', views.template_language),
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('greeting/<str:name>/', views.greeting),
    path('dinner/', views.dinner),
    path('index/', views.index),  # index/ 를 views.index 로 매핑   '/' 로 끝나야 한다
    path('admin/', admin.site.urls),
]
