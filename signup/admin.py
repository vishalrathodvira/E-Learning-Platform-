from django.contrib import admin         
from signup . models import New_Arrivals,All_Product,feedback
from signup . models import Payment,Address,Feature_Product,Header,Bestdeal
# Register your models here.


admin.site.register(Feature_Product)
admin.site.register(Header)
admin.site.register(New_Arrivals)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(All_Product)
admin.site.register(Bestdeal)
admin.site.register(feedback)






class SaveuserAdmin(admin.ModelAdmin):
    list_display = ['id','name','lastname','userid','emailid']


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','email','address','city','state','contry','zip')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','cardname','crno','expmonth','expyear','cvv')

class New_ArrivalsAdmin(admin.ModelAdmin):
    list_display = ('image','name','price','mprice')

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('image','name','price')

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('image','name','price')

class IphoneAdmin(admin.ModelAdmin):
    list_display = ('image','name','price')

class All_ProductAdmin(admin.ModelAdmin):
    list_display = ('image','name','price')

class HeadphoneAdmin(admin.ModelAdmin):
    list_display = ('image','name','price')
