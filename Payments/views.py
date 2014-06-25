from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Payments.forms import *
from Payments.models import *

from .forms import EmployeeAddForm

def main_page(request):
    return render_to_response(
      'main_page.html', RequestContext(request)
    )
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
#-----------------------
@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EmployeeAddForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('employee_add.html', variables)

@login_required
def bank_add(request):
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EmployeeAddForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('bank_add.html', variables)

#----------------------------------------------------------------------
class EmployeeAddFormView(View):
    form_class = EmployeeAddForm
    initial = {'key': 'value'}
    template_name = 'employee_add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


