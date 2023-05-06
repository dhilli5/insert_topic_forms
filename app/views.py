from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *
from app.forms import *



def insert_topic(request):
    TO=TopicForm()
    d={"TO":TO}
    if request.method=="POST":
        TOD=TopicForm(request.POST)
        
        if TOD.is_valid():
            topic_name=TOD.cleaned_data["topic_name"]
            
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TQ=Topic.objects.all()
            d1={"TQ":TQ}

            return render(request,'display_topic.html',d1)
    return render(request,"insert_topic.html",d)
def insert_webpage(request):
    WO=WebpageForm
    
    
