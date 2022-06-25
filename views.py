from django.shortcuts import render,redirect
from .forms import *
from .models import Employee

# Create your views here.
def employee_list(request):
    #context = {'context':Employee.objects.all()}
    data=Employee.objects.all()
    #check=Employee.objects.all()
    return render(request,'employee_list.html',{'context':data})


def employee_form(request,id=0):
    if request.method =='GET':
        if id == 0:
            form = Employee_form()
        else:
            employee = Employee.objects.get(pk=id)
            form = Employee_form(instance=employee)
        return render(request, 'employee_form.html',{'form':form})
    else:
        if id == 0:
            form=Employee_form(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = Employee_form(request.POST,instance=employee)  
        if form.is_valid():
            form.save()
        return redirect('/employee/list')



def employee_delete(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect ('/employee/list')





