from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,
                                    DeleteView)
from . import forms
from foodapp.models import *
from django.urls import reverse_lazy,reverse
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def disp(request):
    data=Model_img.objects.all()
    return render(request,'disp.html',context={'objects':data})

class Form_name(View):
    def get(self,request):
        return render(request,'temp2.html',context={'form':forms.Form_name()})
    
    def post(self,request):
        form=forms.Form_name(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponse("Thank you for registering")
        #return render(request,'temp2.html',context={'form':form})
class loginform(View):
    def get(self,request):
        return render(request,'temp1.html',context={'form':forms.loginform()})
    
    def post(self,request):
        form=forms.loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponse("Login successfull")
        #return render(request,'temp2.html',context={'form':form})
def about(request):
    data={'data':'RSA,is a city in the Indian state of Karnataka. It is the administrative headquarters of Udupi District. It is one of the fastest growing cities in Karnataka & the city has got a modern touch due to various educational institutions. Udupi is one of the top tourist attractions in Karnataka. It is notable for the Krishna Temple. It lends its name to the popular Udupi cuisine. It is also known as Lord Parashurama Kshetra, and is famous for Kanakana Kindi. A centre of pilgrimage, Udupi is known as Rajata Peetha and Shivalli (Shivabelle). It is also known as the temple city.[3] Udupi is situated about 55 km north of the educational, commercial & industrial hub Mangalore and about 422 km west of state capital Bangalore by road.'}
    return render(request,'about1.html',context=data)

def south(request):
    return render(request,'south.html')
def north(request):
    return render(request,'north.html')
def chiense(request):
    return render(request,'chinece.html')
def final(request):
    return render(request,'about.html')