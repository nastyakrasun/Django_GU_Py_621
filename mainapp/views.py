from django.shortcuts import render
from mainapp.models import Product


def products(request):
	title = 'каталог/продукты'
	products = Product.objects.all()[4:]

	links_menu = [
		{'href': 'products_all', 'name': 'все'},
		{'href': 'products_home', 'name': 'дом'},
		{'href': 'mainapp:products', 'name': 'офис'},
		{'href': 'mainapp:products', 'name': 'модерн'},
		{'href': 'mainapp:products', 'name': 'классика'},
	]

	context = {
		'products': products,
		'links_menu': links_menu,
		'title': title,
	}

	return render(request, 'mainapp/products.html', context=context)