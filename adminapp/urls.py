from django.urls import path

import adminapp.views as adminapp_views

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp_views.user_create, name='user_create'),
    path('users/read/', adminapp_views.users, name='users'),
    path('users/update/<int:pk>/', adminapp_views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp_views.user_delete, name='user_delete'),

    path('categories/create/', adminapp_views.category_create, name='category_create'),
    path('categories/read/', adminapp_views.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp_views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp_views.category_delete, name='category_delete'),

    path('products/create/category/<int:pk>/', adminapp_views.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp_views.products, name='products'),
    path('products/read/<int:pk>/', adminapp_views.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp_views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp_views.product_delete, name='product_delete'),
]
