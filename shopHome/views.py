from django.shortcuts import render
from .models import Fashion, Electronic, Jewellery

# Create your views here.

def INDEX(request):
    fashion = Fashion.objects.all()
    electronic = Electronic.objects.all()
    jewellery = Jewellery.objects.all()

    context = {
        'fashion' :fashion,
        'electronic' :electronic,
        'jewellery' :jewellery
    }
    return render(request, 'index.html', context)

    # <!-- fashion section start -->

    # <!-- fashion section end -->



    # <!-- electronic section start -->
    
    # <!-- electronic section end -->



    # <!-- jewellery  section start -->
    
    # <!-- jewellery  section end -->