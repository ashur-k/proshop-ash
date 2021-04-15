from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    
    list_display = ['_id', 'createdAt']



admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)

admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
