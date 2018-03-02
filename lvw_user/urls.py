from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('register_handle', views.register_handle),
    path('login_handle',views.login_handle),
    path('logout',views.logout),
    path('check_name',views.register_exist),
    path('user_info',views.user_center_info),
    path('user_update',views.user_update),
    path('会员中心 - 配送地址',views.user_center_site),
    path('会员中心 - 配送地址2',views.user_center_site2),
    path('add_save',views.add_save),
    path('mrdz',views.mrdz),
    path('scdz',views.scdz),
    path('bjdz',views.bjdz),
]
