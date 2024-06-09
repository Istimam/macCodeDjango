from django.shortcuts import render

# Create your views here.
def add_brand(request):
    return render(request, 'add_brand.html')