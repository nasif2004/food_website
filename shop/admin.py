from django.contrib import admin

from shop.models import categ, product

# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(categ,categadmin)

class proadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','img','stock','available']
    list_editable=['price','img','stock','available']
admin.site.register(product,proadmin)    