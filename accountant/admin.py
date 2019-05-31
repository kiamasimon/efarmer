from django.contrib import admin

# Register your models here.
from accountant.models import Admin_User, Accountant, Stock

admin.site.register(Admin_User)
admin.site.register(Accountant)
admin.site.register(Stock)