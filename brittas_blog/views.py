from django.shortcuts import render
from .models import HomePageContent

# Create your views here.
# brittas_blog/views.py

def home(request):
   content = HomePageContent.objects.first()  # Retrieve the first record, you can modify this based on your needs
   return render(request, 'home.html', {'content': content})

def gallery(request):
    # Your view logic here
    return render(request, 'gallery.html')  # Replace with the actual template name

    brittas_blog/views.py
from django.shortcuts import render


def about(request):
    # Your view logic here
    return render(request, 'about.html')  # Replace with the actual template name