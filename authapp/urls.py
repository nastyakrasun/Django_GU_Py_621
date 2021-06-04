from django.urls import path
from authapp import views as authapp_views

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp_views.login, name='login'),
    path('logout/', authapp_views.logout, name='logout'),
]
