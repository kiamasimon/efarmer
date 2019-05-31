from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accountant.models import Accountant, Product, Sale, Stock, Customer


class SignUpForm(UserCreationForm):

    class Meta:
        model = Accountant
        fields = ('username', 'first_name', 'last_name', 'email', 'location')


class AddStockForm(ModelForm):

    class Meta:
        model = Stock
        fields = ('name',)


class AddCustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number')


class AddProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'stock', 'buying_price')


class AddSaleForm(ModelForm):

    class Meta:
        model = Sale
        fields = ('user', 'customer', 'product', 'price_per_unit', 'units_sold', 'total')