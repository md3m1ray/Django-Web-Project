from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cobtact(request):
    return render(request, 'contact.html')