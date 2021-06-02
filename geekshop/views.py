from django.shortcuts import render
from mainapp.models import Product

def index(request, pk=None):
    if pk:
        print(f'PK -- {pk}')

    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'hELLO',
        'title': title,
    }
    return render(request, 'geekshop/index.html', context=context)


def contact(request):
	return render(request, 'geekshop/contact.html')