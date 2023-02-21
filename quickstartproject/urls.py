from django.contrib import admin
from django.urls import include, path
from hello_azure.templates.hello_azure import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('testa', views.testa, name='testa'),
    path('getquery', views.getquery, name='getquery'),
]
