from django.contrib.auth.models import User
from django.db import models

class Employee (models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.name)

class Payer (models.Model):
    payer = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.payer)

class Activity (models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)

class Category (models.Model):
    category = models.CharField(max_length=200)
    activity = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.SET_NULL)
    incoming = models.BooleanField()
    
    def __unicode__(self):
        return u'%s' % (self.category)

class Subcategory (models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.CharField(max_length=200)
    activity = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return u'%s' % (self.sub_category)

class Bank (models.Model):
    bank_name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.bank_name)

class Counterparty (models.Model):
    name = models.CharField(max_length=200)

class Expense (models.Model):
    budget_holder = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL)
    payer = models.ForeignKey('Payer', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(u'Plan of expenses till')
    amount = models.IntegerField(default=0)
    is_internal = models.BooleanField()
    counterparty = models.ForeignKey('Counterparty', null=True, blank=True, on_delete=models.SET_NULL)
    agreement = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.budget_holder)

class Payment (models.Model):
    payment_date = models.DateField('Payment date')
    initiator = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL)
    payer = models.ForeignKey('Payer', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(default=0)
    conterparty_recipient = models.CharField(max_length=200)
    bill_num = models.CharField(max_length=200)
    bill_date = models.DateField('Date of the bill')
    agreement_num = models.CharField(max_length=200)
    agreement_date = models.DateField('Date of the agreement')
    document = models.CharField(max_length=200)
    attachment = models.CharField(max_length=200)
    bank = models.ForeignKey('Bank', null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=200)
    reestr_num = models.CharField(max_length=200)
    controller_appr = models.BooleanField()
    cfo_appr = models.BooleanField()
    paid = models.BooleanField()
    
    def __unicode__(self):
        return unicode(self.initiator)
