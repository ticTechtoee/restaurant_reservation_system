from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superuser_index', views.index, name='index'),
    path('booking_page', views.reservation, name= "booking_page"),
    path('sorry',views.sorry, name = "Booking_Failed"),
    path('sucess', views.success, name = "Booking_Successful"),

    path('', views.welcome, name="welcome"),

    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

    path('cancel_booking/<str:pk>', views.cancel_booking, name='cancel_booking'),

]
