from django.http import HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: user.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.filter(is_delete=False).order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    title = 'Пользователи/Создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()

            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'create_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    title = 'Пользователи/Редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserRegisterForm(instance=edit_user)

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    title = 'Пользователи/Удаление'

    user_to_delete = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_to_delete.is_delete = True
        user_to_delete.save()

        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'delete_form': user_to_delete,
    }

    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda user: user.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda user: user.is_superuser)
def category_create(request):
    pass


@user_passes_test(lambda user: user.is_superuser)
def category_update(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def category_delete(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda user: user.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, pk):
    pass
