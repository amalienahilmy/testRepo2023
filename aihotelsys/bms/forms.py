from django import forms
from django.forms import ModelForm
from .models import MainXaction

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

class AdditionForm(forms.Form):
    number1 = forms.IntegerField(label='Number 1')
    number2 = forms.IntegerField(label='Number 2')
