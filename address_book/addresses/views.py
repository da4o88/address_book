from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import ClientForm, AddressForm
from .models import Address

# Create your views here.


def show_address(request, address_id):
    address = Address.objects.get(pk=address_id)
    return render(request, 'addresses/show_address.html', {
        "address": address,
    })


def update_address(request, address_id):
    address = Address.objects.get(pk=address_id)
    form = AddressForm(request.POST or None, request.FILES or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('list_address')
    return render(request, 'addresses/update_address.html', {
        "address": address,
        "form": form,
    })


def list_address(request):
    address_list = Address.objects.all()

    return render(request, 'addresses/list_address.html', {
        "address_list": address_list,
    })


def add_address(request):
    submitted = False
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_address?submitted=True')
    else:
        form = AddressForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addresses/add_address.html', {
        "form": form,
        "submitted": submitted,
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )

    # Get current date
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%I:%M %p')

    return render(request, 'addresses/home.html', {
        "year": year,
        "month": month,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })
