from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView,View
from app41.models import EmployeeModel
from django.contrib.messages.views import SuccessMessageMixin


class Home(TemplateView):
    template_name = "home.html"


class AddEmployee(SuccessMessageMixin,CreateView):
    template_name = "add_employee.html"

    model = EmployeeModel

    fields = '__all__'

    success_url = 'add_employee.html'

    success_message = "Employee is Saved"

#view all record
class ViewAllEmployee(ListView):
    template_name = 'view_all_employee.html'

    model = EmployeeModel

#view all rows but specific column
class ViewSpecific(ListView):
    template_name = 'view_specific.html'
    model = EmployeeModel
    queryset = EmployeeModel.objects.values('idno','name','photo')

class AllId(DetailView):
    template_name = 'all_id.html'
    model = EmployeeModel

class UpdateEmployee(UpdateView):
    template_name = 'update.html'
    model = EmployeeModel
    fields = '__all__'
    success_url = '/view_all_employee/'

class DeleteEmployee(DeleteView):
    template_name = 'delete.html'
    model = EmployeeModel
    success_url = '/view_all_employee/'

