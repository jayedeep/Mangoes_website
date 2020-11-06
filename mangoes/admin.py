from django.contrib import admin

# Register your models here.
from .models import CustomUser,Mango_For_Sell,Mangoes_For_Buy,Deliver
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Mango_For_Sell)
admin.site.register(Mangoes_For_Buy)
admin.site.register(Deliver)