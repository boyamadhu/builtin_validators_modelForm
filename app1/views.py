from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.forms import *

def insert_topic(request):
    d={'TO':TopicForm()}

    if request.method=='POST':
        TO1=TopicForm(request.POST)
        if TO1.is_valid():
            TO1.save()
            return HttpResponse('data is inserted successfully')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)