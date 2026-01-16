from django.contrib import admin
from .models import Category,Ovqat


# Register your models here.

@admin.register(Category)   #decorator
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','type']
    ordering = ['id']
    list_display_links = ['id','name','type']
    list_per_page = 5

@admin.register(Ovqat)
class OvqatAdmin(admin.ModelAdmin):
    list_display = ['nom','kategoriya','narx','kkal']
    search_fields = ['nomi']
    list_filter = ['nomi','ctg','narxi','kaloriya']


    @admin.display(empty_value='---', description="Ovqatning Nomi")
    def nom(self,obj,*args,**kwargs):
        return obj.nomi

    @admin.display(empty_value='---', description="Ovqatning Narxi")
    def narx(self,obj,*args,**kwargs):
        return f"{obj.narxi} So'm"

    @admin.display(empty_value='---', description="Ovqatning Kategoriyasi")
    def kategoriya(self,obj,*args,**kwargs):
        return obj.ctg

    @admin.display(empty_value='---', description="Ovqatning Kaloriyasi")
    def kkal(self,obj,*args,**kwargs):
        return f"{obj.kaloriya} Kkal"
