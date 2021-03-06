"""Software_Engineering_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from mainsite.views import index,about,detail,category,register,login,logout,send,apply,message,contact,resume,test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('detail/<int:jobID>',detail),
    path('category/',category),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('login/',login),
    path('logout/',logout),
    path('apply',apply),
    path('send/',send),
    path('message/',message),
    path('resume',resume,name='resume'),
    path('test/',test),
]
