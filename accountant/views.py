from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from accountant.forms import SignUpForm, AddProductForm, AddStockForm, AddCustomerForm, AddSaleForm
from accountant.models import Accountant, Admin_User, Stock, Product, Customer, Sale

app_name = 'Accountant'


def landing(request):
    return render(request, 'accountant/landing_page.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        # pdb.set_trace()
        if form.is_valid():
            farmer = form.save(commit=False)
            farmer.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Farmer:my_sales')
        else:
            messages.error(request, 'Form Invalid')
            return redirect('Accounts:signup')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html',{'form':form})


def sign_in(request):
    msg = []

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if Accountant.objects.filter(user_ptr_id=user.id).exists():
                    return redirect('Accountant:dashboard')
                elif Admin_User.objects.filter(user_ptr_id=user.id).exists():
                    return redirect('Accountant:dashboard')
            else:
                msg.append('You account has been deactivated!')
    else:
        msg.append('Invalid login')
    return render(request, 'registration/sign_in.html', {'errors':msg})


def stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'accountant/view_stocks.html', {'stocks':stocks})


def new_stock(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock Added Successfully')
            return redirect('Accountant:stocks')
        else:
            messages.error(request, 'Invalid Details Please Try Again')
    return render(request, 'accountant/add_stock.html')


def products(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    products = Product.objects.filter(stock=stock)
    return render(request, 'accountant/view_products.html', {'products':products, 'stock':stock})


def new_product(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    form = AddProductForm(request.POST)

    if request.method == 'POST':
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Added Successfully')
            return redirect('Accountant:products', stock.id)
        else:
            messages.error(request, 'Failed to add the product')
            return redirect('Accountant:new_product', stock.id)
    else:
        form = AddProductForm()
        return render(request, 'accountant/add_product.html',{'stock':stock, 'form':form})


def dashboard(request):
    return render(request, 'layouts/base.html')


def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'accountant/customers.html', context)


def add_customer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Added Successfully')
            return redirect('Accountant:customers')
        else:
            messages.error(request, 'Form Validation Failed')
            return redirect('Accountant:customers')
    return render(request, 'accountant/add_customer.html')


def sales(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer_sales = Sale.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'customer_sales': customer_sales
    }
    return render(request, 'accountant/sales.html', context)


def add_sale(request, customer_id):
    admin = Admin_User.objects.get(user_ptr_id = request.user.id)
    customer = Customer.objects.get(id=customer_id)
    products = Product.objects.all()
    if request.method == 'POST':
        form = AddSaleForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sale added successfully')
            return redirect('Accountant:sales', customer_id)
        else:
            messages.error(request, 'Form Validation Failed')
            return redirect('Accountant:sales', customer_id)

    context = {
        'admin': admin,
        'customer': customer,
        'products': products
    }
    return render(request, 'accountant/add_sale.html', context)