from django.db import models
from .base.base import BaseModel
from django.db.models import Sum
from django_countries.fields import CountryField
from django.utils import timezone
from datetime import datetime, timedelta



class Hotel(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # Add more fields as per your requirements
    def __str__(self):
        return self.name
    
class IncomeSource(BaseModel):
    abbreviation = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class ExpenseSource(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class MainXaction(BaseModel):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    date = models.DateField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    expense_source = models.ForeignKey(ExpenseSource, on_delete=models.PROTECT, null=True, blank=True)
    income_source = models.ForeignKey(IncomeSource, on_delete=models.PROTECT, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=Hotel.objects.first)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_due = models.BooleanField(default=False)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.remark}"
    
    @staticmethod
    def get_sum_expense_by_expense_source():
        expense_sums = MainXaction.objects.filter(transaction_type='expense').values('expense_source').annotate(total_amount=Sum('amount'))
        return expense_sums


class Client(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=Hotel.objects.first)
    fullname = models.CharField(max_length=50)
    country = CountryField()
    phone_number =  models.CharField(max_length=20, null=True, blank=True)
    nric_passport = models.CharField(max_length=30, null=True, blank=True)
    isBlacklisted =  models.BooleanField(default=False)
    isRegular =  models.BooleanField(default=False)

    def __str__(self):
        return self.fullname 
    
    
class RoomType(BaseModel):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name 

    
class Room(BaseModel):
    room_number = models.CharField(max_length=7)
    room_type = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING, default='0000')
    isWindow =  models.BooleanField(default=False)
    remark = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.room_number 
    

class BookingPlatform(BaseModel):
    abbreviation = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class PaymentMethod(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    isActive = models.BooleanField(default=True)
    remark =  models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    



class Booking(BaseModel):

    cash_payment_method = PaymentMethod.objects.get(name="Cash")

    now = datetime.now()
    # Calculate tomorrow's datetime at 2 PM
    tomorrow_datetime = now + timedelta(days=1)
    tomorrow = tomorrow_datetime.replace(hour=14, minute=0, second=0, microsecond=0)


    checkin_date = models.DateTimeField(default=now)
    checkout_date = models.DateTimeField(default=tomorrow)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete= models.DO_NOTHING)
    platform = models.ForeignKey(BookingPlatform, on_delete=models.DO_NOTHING)
    booking_reference = models.CharField(max_length=30, null=True, blank=True)
    amount_deposit = models.DecimalField(max_digits=8, decimal_places=2)
    total_room_price = models.DecimalField(max_digits=8, decimal_places=2)   # how to auto populate room price based on selected room?
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)  
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, default=cash_payment_method.pk)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)

    print (now)
    print (tomorrow)

    
    def __str__(self):
        return f"self.checkin_date"
    