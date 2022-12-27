from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import ClientForm, AddressForm
from .models import Address

# Import Pagination Stuff
from django.core.paginator import Paginator

# Create your views here.


def show_address(request, address_id):
    address = Address.objects.get(pk=address_id)
    return render(request, 'addresses/show_address.html', {
        "address": address,
    })


def delete_address(request, address_id):
    address = Address.objects.get(pk=address_id)
    address.delete()
    messages.success(request, "Address Deleted!!!")
    return redirect('list_address')


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
    all_address = Address.objects.all()

    return render(request, 'addresses/list_address.html', {
        "all_address": all_address,
    })


def address_list(request):
    address_to_list = Address.objects.all().order_by('street_name')

    # Set up Pagination
    p = Paginator(Address.objects.all(), 2)
    page = request.GET.get('page')
    page_address = p.get_page(page)
    nums = "a" * page_address.paginator.num_pages

    return render(request, 'addresses/list_address.html',
                  {
                      "address_to_list": address_to_list,
                      'page_address': page_address,
                      'nums': nums,
                  })


def add_address(request):
    submitted = False
    address_list = Address.objects.all()
    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            street_name = form.cleaned_data['street_name']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            country = form.cleaned_data['country']

            # Check if address is already in DB
            for address in address_list:
                if street_name == address.street_name and city == address.city and zip_code == address.zip_code \
                        and country == address.country:
                    messages.success(request, 'Address already exists!!')
                    return redirect('list_address')
            else:
                form.save()
                return HttpResponseRedirect('/add_address?submitted=True')
    else:
        form = AddressForm
        if 'submitted' in request.GET:
            submitted = True
            messages.success(request, "Address was added successfully!!!")
            return redirect('list_address')

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
