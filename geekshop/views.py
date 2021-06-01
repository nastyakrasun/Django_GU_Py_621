from django.shortcuts import render


def index(request):
    list_params = ['a1', 'a2', 'a3']
    context = {'dict_params': list_params, 'some_name': 'hELLO'}
    return render(request, 'geekshop/index.html', context=context)


def contact(request):
	return render(request, 'geekshop/contact.html')