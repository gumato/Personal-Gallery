from django.http  import HttpResponse,Http404
from django.shortcuts import render
import datetime as dt

# Create your views here.
def mygallery(request):
    date = dt.date.today()
     
    return render(request,'welcome.html',{"date": date})
