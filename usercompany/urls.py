from django.conf.urls import url

from usercompany import views
from django.urls import path
urlpatterns = [
    path('home/', views.company_home, name='company_home'),
    path('stock/add', views.add_stock, name='add_stock_company'),
    path('stock/view', views.view_stocks, name='view_stock_company'),
    path('stock/avail_view', views.view_avail_stocks, name='view_avail_stock_company'),
    path('stock/<pk>/edit', views.edit_stock, name='edit_stock_company'),
    path('stock/<pk>/delete', views.delete_stock, name='delete_stock_company'),

    path('order/view', views.view_orders, name='view_order_company'),
    path('order/<pk>/accept', views.accept_order, name='accept_order_company'),
    path('order/<pk>/decline', views.decline_order, name='decline_order_company'),

    path('transactions/view', views.view_transactions, name='view_transactions_company'),
]
