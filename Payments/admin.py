from django.contrib import admin
from Payments.models import * 

class PaymentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee)
admin.site.register(Payer)
admin.site.register(Category)
admin.site.register(Bank)
admin.site.register(Expense)
admin.site.register(Subcategory)
admin.site.register(Payment)
admin.site.register(Activity)
admin.site.register(Counterparty)
