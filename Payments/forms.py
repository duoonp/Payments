from django.forms import ModelForm
from Payments.models import *#Payment, Expense, Employee, Payer, Category, Subcategory, Bank, ActivCounterparty

class PaymentAddForm(ModelForm):
    class Meta:
        model = Payment

class ExpenseAddForm(ModelForm):
    class Meta:
        model = Expense

class EmployeeAddForm(ModelForm):
    class Meta:
        model = Employee

class PayerAddForm(ModelForm):
    class Meta:
        model = Payer

class CategoryAddForm(ModelForm):
    class Meta:
        model = Category

class SubcategoryAddForm(ModelForm):
    class Meta:
        model = Subcategory

class BankAddForm(ModelForm):
    class Meta:
        model = Bank

class ActivityAddForm(ModelForm):
    class Meta:
        model = Activity

class CounterpartyAddForm(ModelForm):
    class Meta:
        model = Counterparty



