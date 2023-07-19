from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from .forms import EmployeeEditForm
# Create your views here.
def index(request):
    return render(request, 'base.html')

def view(request):
    employees = Employee.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        employees = employees.filter(emp_id__startswith=search_query)
    return render(request, 'view.html', {'employees': employees})

def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
            
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {'form': form})

def update(request):
    employees = Employee.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        employees = employees.filter(emp_id__startswith=search_query)
    return render(request, 'update.html', {'employees': employees})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('update')
    else:
        form = EmployeeEditForm(instance=employee)
    
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('update')
    
    return render(request, 'delete_employee.html', {'employee': employee})


