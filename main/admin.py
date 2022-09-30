from django.contrib import admin
from .models import Restaurant, Table,Seat, Reservation, Menu


admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Seat)
admin.site.register(Reservation)
admin.site.register(Menu)