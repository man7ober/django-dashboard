from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from employee.forms import EmployeeForm  
from employee.models import Employee
import datetime

# Create your views here.

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):
    employees = Employee.objects.all().order_by('eid')
    calendar = {
        'day': (datetime.datetime.now()).strftime("%d"),
        'month': (datetime.datetime.now()).strftime("%B"),
        'year': (datetime.datetime.now()).strftime("%Y")
    }

    time = {
        'hour': (datetime.datetime.now()).strftime("%I"),
        'minute': (datetime.datetime.now()).strftime("%M"),
        'midday': (datetime.datetime.now()).strftime("%p")
    }
    

    return render(request,"show.html",{'employees':employees,'calendar': calendar, 'time': time}) 

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  

def search(request, id):
    form =  Employee.objects.get(id=id)
    print(frorm)  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")