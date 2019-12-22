"""food URL Configuration

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
    1. Import the include() function: from django.urls import include,path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from foodapp import views
import foodapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('template_demo/',views.Form_name.as_view(),name="temp2"),
    path('login_demo/',views.loginform.as_view(),name="temp1"),
    path('food/',include("foodapp.urls")),
    path('about/',views.about,name="about"),
    path('south/',views.south,name="south"),
    path('north/',views.north,name="north"),
    path('chiense/',views.chiense,name="chiense"),
    path('final/',views.final,name="final"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#changing admin site
admin.site.site_header='RSA FOOD'

