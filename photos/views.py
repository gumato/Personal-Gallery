from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def mygallery(request):
    date = dt.date.today()
    photos = Image.get_all()

    return render(request,'all-photos/home.html',{"date": date,"photos":photos})
