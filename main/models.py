from email.policy import default
from django.db import models
from django.db.models import Model

class Reservation(models.Model):
  Name = models.CharField(default = 'None', max_length = 30)
  Restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT)
  Booking_time = models.DateTimeField(null=False, blank=False, unique=True)
  def __str__(self):
      return self.Name
  
 
class Restaurant(models.Model):
  name = models.CharField(max_length=20)
  def __str__(self):
      return self.name
  

class Table(models.Model):
  restaurant = models.ForeignKey("Restaurant", on_delete = models.PROTECT)
  table_number = models.CharField(max_length = 2, default = "0")
  def __str__(self):
      return self.table_number
  

class Seat(models.Model):
  table = models.ForeignKey("Table", on_delete = models.PROTECT)
  total_seats = models.IntegerField(default = 6)
  occupied_seats = models.IntegerField(default = 0)

class Menu(models.Model):
  name = models.CharField(max_length = 30, default = "None")

  def __str__(self) -> str:
     return self.name

#free_tables = my_restaurant.table_set.exclude(reservation_set__booking_time=selected_datetime)