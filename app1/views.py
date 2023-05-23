from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *
# Create your views here.
from django.views import View

def function_string(request):
    return HttpResponse('this is function')

class class_string(View):
    def get(self,request):
        return HttpResponse('this is class')

def function_html(request):
    return render(request,'first.html')

class class_html(View):
    def get(self,request):
        return render(request,'first.html')
    
def function_form(request):
    T=TopicForm()
    d={'T':T}
    if request.method=='POST':
        TO=TopicForm(request.POST)
        if TO.is_valid():
            TO.save()
            return HttpResponse('submiting success')
    return render(request,'form.html',d)

class class_form(View):
    def get(self,request):
        T=TopicForm()
        d={'T':T}
        return render(request,'form.html',d)
    
    def post(self,request):
        TO=TopicForm(request.POST)
        if TO.is_valid():
            TO.save()
            return HttpResponse('sumitted success')