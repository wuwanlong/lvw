from django.urls import path
from lvw_goods.views import index

urlpatterns = [
    path('', index, name='index'),
]
