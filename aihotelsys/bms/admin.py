from django.contrib import admin
from .models import Hotel
from .models import ExpenseSource, MainXaction, Client, Booking, Room, RoomType, BookingPlatform, PaymentMethod

# Register your models here.

admin.site.register(Hotel)
admin.site.register(ExpenseSource)
admin.site.register(MainXaction)
admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(BookingPlatform)
admin.site.register(PaymentMethod)