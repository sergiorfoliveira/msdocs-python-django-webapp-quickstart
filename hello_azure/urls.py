from django.urls import path
from hello_azure.templates.hello_azure import views
#
# urlpatterns = [path('', views.index, name='index'),
#                path('index', views.index, name='index'),
#                path('testa', views.testa, name='testa'),
#                path('getquery', views.getquery(), name='getquery')
#                ]
urlpatterns = [
    path('index', views.index, name='index'),
    path('testa', views.testa, name='testa'),
    path('getquery', views.getquery, name='getquery')
]
