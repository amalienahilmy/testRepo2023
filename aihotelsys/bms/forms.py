from django import forms
from django.forms import ModelForm
from .models import MainXaction, Client, Booking
from django.forms.widgets import DateTimeInput

class IncomeXactionForm(ModelForm):
    transaction_type = forms.CharField(initial='income')
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model = MainXaction
        exclude = ['expense_source', 'updated_by', 'hotel', 'is_deleted']
        widgets = {
            'transaction_type': forms.Select(attrs={'data-category': 'transaction-category'}),
            'expense_source': forms.Select(attrs={'data-category': 'expense-category'}),
            'income_source': forms.Select(attrs={'data-category': 'income-category'}),
            'amount': forms.NumberInput(attrs={'data-category': 'amount-category'}),
            'is_due': forms.CheckboxInput(attrs={'data-category': 'is-due-category'}),
            'amount_due': forms.NumberInput(attrs={'data-category': 'amount-due-category'}),
            'remark': forms.TextInput(attrs={'data-category': 'remark-category'}),
        }

class ExpenseXactionForm(ModelForm):
    transaction_type = forms.CharField(initial='expense')
    class Meta:
        model = MainXaction
        exclude = ['income_source', 'updated_by', 'hotel', 'is_deleted']
        widgets = {
            'transaction_type': forms.Select(attrs={'data-category': 'transaction-category'}),
            'expense_source': forms.Select(attrs={'data-category': 'expense-category'}),
            'income_source': forms.Select(attrs={'data-category': 'income-category'}),
            'amount': forms.NumberInput(attrs={'data-category': 'amount-category'}),
            'is_due': forms.CheckboxInput(attrs={'data-category': 'is-due-category'}),
            'amount_due': forms.NumberInput(attrs={'data-category': 'amount-due-category'}),
            'remark': forms.TextInput(attrs={'data-category': 'remark-category'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # fields = "__all__"   #Show all fields
        fields = (
            'checkin_date','checkout_date','client', 
            'room','platform','booking_reference','amount_deposit',
            'total_room_price','amount_paid','payment_method' 
        )

        labels = {
              'checkin_date': 'Check In Date & Time'
            ,'checkout_date': 'Check Out Date & Time'
            ,'client': 'Client'
            ,'room': 'Room'
            ,'platform': 'Platform'
            ,'booking_reference': 'Booking ID'
            ,'amount_deposit': 'Deposit Amount'
            ,'total_room_price': 'Room Price'
            ,'amount_paid': 'Paid Amount'
            ,'payment_method': 'Payment Method'
        }

        widgets={
            'checkin_date': DateTimeInput(attrs={'class':'form-control'})
            ,'checkout_date': DateTimeInput(attrs={'class':'form-control'})
            ,'client': forms.Select(attrs={'class':'form-control'})
            ,'room': forms.Select(attrs={'class':'form-control'})
            ,'platform': forms.Select(attrs={'class':'form-control'})
            ,'booking_reference': forms.TextInput (attrs={'class':'form-control','placeholder':'Booking ID'})
            ,'amount_deposit': forms.NumberInput (attrs={'class':'form-control','placeholder':'Amount Deposit'})
            ,'total_room_price': forms.NumberInput (attrs={'class':'form-control','placeholder':'Room Price'})
            ,'amount_paid': forms.NumberInput (attrs={'class':'form-control','placeholder':'Total Amount Paid'})
            ,'payment_method': forms.Select(attrs={'class':'form-control'}),
        }