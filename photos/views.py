from django.http  import HttpResponse,Http404
from django.shortcuts import render

import datetime as dt
from .models import Image

# Create your views here.
def gallery(request):
    images=Image.objects.all()
    return render(request, 'gallery.html',{"images": images })

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any Image Category"
        return render(request, 'all-photos/search.html',{"message":message})
     
    return render(request,'welcome.html',{"date": date})
