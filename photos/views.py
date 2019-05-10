from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.
def mygallery(request):
    date = dt.date.today()
    # photos = Image.get_all()

    return render(request,'welcome.html',{"date": date})
