from django.shortcuts import render, redirect
from cars.models import Car
from brands.models import CarBrand

def home(request):
    model = request.GET.get('model')
    if model:
        data = Car.objects.filter(brand__name=model)
    else:
        data = Car.objects.all()
    
    cars = CarBrand.objects.all()
    brand_counts = {car_brand.name: Car.objects.filter(brand = car_brand).count()
                    for car_brand in cars
                    }
    context = {
        'data': data,
        'cars': cars,
        'brand_counts': brand_counts,
    }
    return render(request, 'home.html', context)
