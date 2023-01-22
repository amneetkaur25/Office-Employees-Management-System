from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.db.models import Q
from emp_app.models import Employee,Department,Role

def index(request):
    return render(request,"index.html")

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"all_emp.html",context)



def add_emp(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        role=request.POST.get('role')
        salary=int(request.POST.get('salary'))
        bonus=int(request.POST.get('bonus'))
        phone=int(request.POST.get('phone'))
        dept=int(request.POST.get('dept'))
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,role_id=role,dept_id=dept,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Sucessfully!!!!")
    elif request.method=="GET":
        return render(request,"add_emp.html")
    else:
        return HttpResponse("Error occured")

    

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Error")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains = dept)
        if role:
            emps=emps.filter(role__name__icontains = role)
        context={
            'emps':emps
        }
        print(context)
        return render(request,"all_emp.html",context)
    elif request.method=="GET":
        return render(request,"filter_emp.html")
    else:
        return HttpResponse("Error Occured")
