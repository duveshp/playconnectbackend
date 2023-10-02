from django.contrib import admin
from .models import PlayAreaDB,VendorDB,UserDB,BookingDB,AdminDB
# Register your models here.

class PlayAreaDBAdmin(admin.ModelAdmin):
    list_display = ('id', 'playAreaName', 'playAreaLocation')
    list_filter = ('playAreaName', 'playAreaLocation','playAreaSports')
    search_fields = ('playAreaName', 'playAreaLocation','playAreaSports')

class VendorDBAdmin(admin.ModelAdmin):
    list_display = ('id', 'VendorName','VendorPlayAreaName', 'VendorPlayAreaLocation')
    list_filter = ('VendorName','VendorPlayAreaName', 'VendorPlayAreaLocation','VendorPlayAreaPrice')
    search_fields = ('VendorPlayAreaName', 'VendorPlayAreaLocation','VendorPlayAreaSports')

class UserDBAdmin(admin.ModelAdmin):
    list_display = ('id', 'userName','userPhoneNo', 'userLocation')
    list_filter = ('userName','userPhoneNo', 'userEmail','userLocation','userAge')
    search_fields = ('userName', 'userPhoneNo','userEmail')

class BookingDBAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookingPlayAreaName','bookingPlayAreaDate', 'bookingPlayAreaUser')
    list_filter = ('bookingPlayAreaName', 'bookingPlayAreaDate','bookingPlayAreaVendor','bookingPlayAreaUser')
    search_fields = ('bookingPlayAreaName', 'bookingPlayAreaVendor')

class AdminDBAdmin(admin.ModelAdmin):
    list_display = ('id', 'adminUserName')
    list_filter = ('adminUserName', 'adminUserLocation')
    search_fields = ('adminUserName', 'adminUserLocation')


admin.site.register(PlayAreaDB, PlayAreaDBAdmin)   
admin.site.register(VendorDB, VendorDBAdmin) 
admin.site.register(UserDB, UserDBAdmin)
admin.site.register(BookingDB, BookingDBAdmin)
admin.site.register(AdminDB, AdminDBAdmin)

