from django.shortcuts import render, redirect
from .models import Restaurant,Reservation,Table

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate,logout

def index(request):
    get_data =  Reservation.objects.all()
    context = {'Table_data': get_data}
    return render(request, 'main/index.html', context)

def welcome(request):
    return render(request, 'main/welcome.html')


def reservation(request):
    get_the_restuarant = Restaurant.objects.all()
    username = None
    if request.method == 'POST':
        get_number_of_guests = request.POST.get('nmbr_of_guests')
        get_Restaurant_name = request.POST.get('get_restaurant_name')
        get_date = request.POST.get('select_date')
        get_time = request.POST.get('select_time')
        if request.user.is_authenticated:
            username = request.user.username
        try:
            order_exists = Reservation.objects.get(Booking_time = str(get_date) +"T"+ str(get_time), Restaurant__name = get_Restaurant_name)
            return redirect('Booking_Failed')
        except Reservation.DoesNotExist:
            get_restaurant = Restaurant.objects.get(name = get_Restaurant_name)
            create_booking = Reservation.objects.create(Name = username, Restaurant = get_restaurant, Booking_time = get_date +"T"+get_time)
            create_booking.save()
            return redirect('Booking_Successful')
    context = {'restaurant_name': get_the_restuarant}  
    return render(request, 'main/book_your_table.html', context)

def sorry(request):
    return render(request, 'main/sorry.html')

def success(request):
 
    return render(request, 'main/success.html')



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if request.user.is_superuser:
                    return redirect("index")
                else:    
                    return redirect("booking_page")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def cancel_booking(request, pk):
    booking_id = Reservation.objects.get(id = pk)
    booking_id.delete()
    return render(request, 'main/index.html')

