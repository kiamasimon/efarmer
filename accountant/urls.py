from django.urls import path

from accountant import views
app_name = 'Accountant'
urlpatterns = [
    path('landing_page', views.landing, name='landing_page'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('stocks', views.stocks, name='stocks'),
    path('products/<int:stock_id>', views.products, name='products'),
    path('new/product/<int:stock_id>', views.new_product, name='new_product'),
    path('new/stock', views.new_stock, name='new_stock'),
    path('customers', views.customers, name='customers'),
    path('customer/sales/<int:customer_id>', views.sales, name='sales'),
    path('add/customer', views.add_customer, name='add_customer'),
    path('add/customer/sale/<int:customer_id>', views.add_sale, name='add_sale')
]