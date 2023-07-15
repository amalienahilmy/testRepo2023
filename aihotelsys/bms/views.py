from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import MainXaction, Client
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers

from .forms import IncomeXactionForm, ExpenseXactionForm, BookingForm


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

def calendar (request):
    return render(request, 'calendar.html')

@login_required
def booking (request):
    return render(request, 'booking.html', {})

@login_required
def client (request):
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})

def get_client(request):
    search = request.GET.get('search')
    payload = []

    if search:
        objs = Client.objects.filter(fullname__startswith=search)
        payload = serializers.serialize('json', objs, fields=('fullname'))

    return JsonResponse({
        'status': True,
        'payload': payload
    }, safe=False)


def finance(request):
    income_form = IncomeXactionForm(prefix='income')  # Add prefix to the income form
    expense_form = ExpenseXactionForm(prefix='expense')  # Add prefix to the expense form

    print('We are in finance')

    if request.method == 'POST':
        print('We are in POST')
        if 'expense_submit' in request.POST:
            expense_form = ExpenseXactionForm(request.POST, prefix='expense')  # Add prefix to the expense form
            if expense_form.is_valid():
                expense_form.save()  # Save the expense form data to the database
                expense_form = ExpenseXactionForm(prefix='expense')  # Reset the expense form
                messages.success(request, 'Expense form submitted successfully')  # Display success message

        elif 'income_submit' in request.POST:
            
            print('we are in income post')
            income_form = IncomeXactionForm(request.POST, prefix='income')  # Add prefix to the income form
            if income_form.is_valid():
                income_form.save()  # Save the income form data to the database
                income_form = IncomeXactionForm(prefix='income')  # Reset the income form
                messages.success(request, 'Income form submitted successfully')  # Display success message

    return render(request, 'finance.html', {'income_form': income_form, 'expense_form': expense_form})


def logout_view(request):
    logout(request)
    return redirect(login_view)

def add_booking(request):

    submitted = False

    if request.method == "POST":
        submitted = False
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_booking?submitted=True')
        
    else:
        form = BookingForm()  # Instantiate the BookingForm class
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_booking.html', {'form': form, 'submitted': submitted})
