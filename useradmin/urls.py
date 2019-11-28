from django.conf.urls import url

from useradmin import views
from django.urls import path
urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('approve/', views.approve, name='approve'),
    path('medicine/add', views.add_medicine, name='add_medicine'),
    path('medicine/view', views.view_medicines, name='view_medicines'),
    path('shop/', views.shop, name='admin_shop_list'),
    path('company/', views.company, name='admin_company_list'),
]
