from django.contrib import admin

from cart.models import cartlist, item

# Register your models here.
admin.site.register(cartlist)
admin.site.register(item)