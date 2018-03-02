from django.urls import path, re_path
from lvw_goods.views import *
from . import views
urlpatterns = [
    path('', index, name='index'),
    re_path('^list_(\d+)_(\d+)_(\d+)$', typelist),
    re_path('^(\d+)$',views.detail),
]
