from django.contrib import admin
from .models import Maktab,Oquvchi

# Restoran:
from .models import Restoran, Mijoz, Xodim, Taom, Stol, Buyurtma, BuyurtmaTafsilot


# Register your models here.

admin.site.register(Maktab)
admin.site.register(Oquvchi)

# Restoran Registratsiyasi:

admin.site.register(Restoran)
admin.site.register(Mijoz)
admin.site.register(Xodim)
admin.site.register(Taom)
admin.site.register(Stol)
admin.site.register(Buyurtma)
admin.site.register(BuyurtmaTafsilot)



