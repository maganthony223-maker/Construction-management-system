from django.shortcuts import render, redirect, get_object_or_404
from .models import clients
from .models import department
from .models import employees as EmployeeModel, department
from .models import projects, clients
from .models import supplier
from .models import materials, supplier
from .models import payments, projects
from .models import projectassignment, employees, projects
from .models import projects as ProjectModel, clients
from .models import projects, clients, supplier



# Create your views here.

def index(request):
    return render (request, 'index.html')

def login(request):
    return render (request, 'login.html')


def clients_view(request):
    if request.method == 'POST':
        clients.objects.create(
            Full_Name=request.POST.get('Full_Name'),
            Phone_Number=request.POST.get('Phone_Number'),
            Email=request.POST.get('Email'),
            Address=request.POST.get('Address')
        )

        return redirect('clients')

    all_clients = clients.objects.all()

    return render(request, 'clients.html', {
        'clients': all_clients
    })
def update_client(request, id):
    client = get_object_or_404(clients, id=id)

    if request.method == 'POST':
        client.Full_Name = request.POST.get('Full_Name')
        client.Phone_Number = request.POST.get('Phone_Number')
        client.Email = request.POST.get('Email')
        client.Address = request.POST.get('Address')

        client.save()

        return redirect('clients')

    return render(request, 'update_client.html', {
        'client': client
    })


def delete_client(request, id):
    if request.method == 'POST':
        client = get_object_or_404(clients, id=id)
        client.delete()

    return redirect('clients')

def department_view(request):
    if request.method == 'POST':
        department.objects.create(
            Department_Name=request.POST.get('Department_Name'),
            Office_Location=request.POST.get('Office_Location')
        )

        return redirect('department')

    all_departments = department.objects.all()

    return render(request, 'department.html', {
        'departments': all_departments
    })


def update_department(request, id):
    dept = get_object_or_404(department, id=id)

    if request.method == 'POST':
        dept.Department_Name = request.POST.get('Department_Name')
        dept.Office_Location = request.POST.get('Office_Location')

        dept.save()

        return redirect('department')

    return render(request, 'update_department.html', {
        'dept': dept
    })



def delete_department(request, id):
    if request.method == 'POST':
        dept = get_object_or_404(department, id=id)
        dept.delete()

    return redirect('department')

def employees_view(request):
    all_departments = department.objects.all()

    if request.method == 'POST':
        selected_department = department.objects.get(
            id=request.POST.get('Department')
        )

        EmployeeModel.objects.create(
            FirstName=request.POST.get('FirstName'),
            LastName=request.POST.get('LastName'),
            Gender=request.POST.get('Gender'),
            Position=request.POST.get('Position'),
            Salary=request.POST.get('Salary'),
            Hire_Date=request.POST.get('Hire_Date'),
            Department=selected_department
        )

        return redirect('employees')

    all_employees = EmployeeModel.objects.all()

    return render(request, 'employees.html', {
        'employees': all_employees,
        'departments': all_departments
    })


def update_employee(request, id):
    employee = get_object_or_404(EmployeeModel, id=id)

    all_departments = department.objects.all()

    if request.method == 'POST':
        employee.FirstName = request.POST.get('FirstName')
        employee.LastName = request.POST.get('LastName')
        employee.Gender = request.POST.get('Gender')
        employee.Position = request.POST.get('Position')
        employee.Salary = request.POST.get('Salary')
        employee.Hire_Date = request.POST.get('Hire_Date')

        selected_department = department.objects.get(
            id=request.POST.get('Department')
        )

        employee.Department = selected_department
        employee.save()

        return redirect('employees')

    return render(request, 'update_employee.html', {
        'employee': employee,
        'departments': all_departments
    })



def delete_employee(request, id):
    if request.method == 'POST':
        employee = get_object_or_404(EmployeeModel, id=id)
        employee.delete()

    return redirect('employees')

def projects_view(request):
    all_clients = clients.objects.all()

    if request.method == 'POST':
        selected_client = clients.objects.get(
            id=request.POST.get('Client')
        )

        ProjectModel.objects.create(
            ProjectName=request.POST.get('ProjectName'),
            Location=request.POST.get('Location'),
            Budget=request.POST.get('Budget'),
            Status=request.POST.get('Status'),
            Client=selected_client
        )

        return redirect('projects')

    all_projects = ProjectModel.objects.all()

    return render(request, 'projects.html', {
        'projects': all_projects,
        'clients': all_clients
    })
    if request.method == 'POST':
        selected_client = clients.objects.get(
            id=request.POST.get('Client')
        )

        projects.objects.create(
            ProjectName=request.POST.get('ProjectName'),
            Location=request.POST.get('Location'),
            Budget=request.POST.get('Budget'),
            Status=request.POST.get('Status'),
            Client=selected_client
        )

        return redirect('projects')

    all_projects = projects.objects.all()
    all_clients = clients.objects.all()

    return render(request, 'projects.html', {
        'projects': all_projects,
        'clients': all_clients
    })


def update_project(request, id):
    project = get_object_or_404(projects, id=id)
    all_clients = clients.objects.all()

    if request.method == 'POST':
        project.ProjectName = request.POST.get('ProjectName')
        project.Location = request.POST.get('Location')
        project.Budget = request.POST.get('Budget')
        project.Status = request.POST.get('Status')

        selected_client = get_object_or_404(
            clients,
            id=request.POST.get('Client')
        )

        project.Client = selected_client
        project.save()

        return redirect('projects')

    return render(request, 'update_projects.html', {
        'project': project,
        'clients': all_clients
    })


def delete_project(request, id):
    if request.method == 'POST':
        project = get_object_or_404(projects, id=id)
        project.delete()

    return redirect('projects')

def supplier_view(request):
    if request.method == 'POST':
        supplier.objects.create(
            SupplierName=request.POST.get('SupplierName'),
            PhoneNumber=request.POST.get('PhoneNumber'),
            Email=request.POST.get('Email'),
            Address=request.POST.get('Address')
        )

        return redirect('supplier')

    all_suppliers = supplier.objects.all()

    return render(request, 'supplier.html', {
        'suppliers': all_suppliers
    })

def update_supplier(request, id):
    selected_supplier = supplier.objects.get(id=id)

    if request.method == 'POST':
        selected_supplier.SupplierName = request.POST.get('SupplierName')
        selected_supplier.PhoneNumber = request.POST.get('PhoneNumber')
        selected_supplier.Email = request.POST.get('Email')
        selected_supplier.Address = request.POST.get('Address')

        selected_supplier.save()

        return redirect('supplier')

    return render(request, 'update_supplier.html', {
        'supplier': selected_supplier
    })


def delete_supplier(request, id):
    if request.method == 'POST':
        selected_supplier = supplier.objects.get(id=id)
        selected_supplier.delete()

    return redirect('supplier')
def materials_view(request):

    if request.method == 'POST':

        selected_supplier = supplier.objects.get(
            id=request.POST.get('Supplier')
        )

        materials.objects.create(
            MaterialName=request.POST.get('MaterialName'),
            UnitPrice=request.POST.get('UnitPrice'),
            QuantityInStock=request.POST.get('QuantityInStock'),
            Supplier=selected_supplier
        )

        return redirect('materials')

    all_materials = materials.objects.all()
    all_suppliers = supplier.objects.all()

    return render(request, 'materials.html', {
        'materials': all_materials,
        'suppliers': all_suppliers
    })

def update_material(request, id):
    material = get_object_or_404(materials, id=id)
    all_suppliers = supplier.objects.all()

    if request.method == 'POST':
        material.MaterialName = request.POST.get('MaterialName')
        material.UnitPrice = request.POST.get('UnitPrice')
        material.QuantityInStock = request.POST.get('QuantityInStock')

        selected_supplier = get_object_or_404(
            supplier,
            id=request.POST.get('Supplier')
        )

        material.Supplier = selected_supplier
        material.save()

        return redirect('materials')

    return render(request, 'update_materials.html', {
        'material': material,
        'suppliers': all_suppliers
    })

def delete_material(request, id):
    if request.method == 'POST':
        material = get_object_or_404(materials, id=id)
        material.delete()

    return redirect('materials')

def payments_view(request):

    if request.method == 'POST':

        selected_project = projects.objects.get(
            id=request.POST.get('Project')
        )

        payments.objects.create(
            Project=selected_project,
            AmountPaid=request.POST.get('AmountPaid'),
            PaymentDate=request.POST.get('PaymentDate'),
            PaymentMethod=request.POST.get('PaymentMethod')
        )

        return redirect('payments')

    all_payments = payments.objects.all()
    all_projects = projects.objects.all()

    return render(request, 'payments.html', {
        'payments': all_payments,
        'projects': all_projects
    })

def update_payment(request, id):
    payment = get_object_or_404(payments, id=id)
    all_projects = projects.objects.all()

    if request.method == 'POST':
        payment.AmountPaid = request.POST.get('AmountPaid')
        payment.PaymentDate = request.POST.get('PaymentDate')
        payment.PaymentMethod = request.POST.get('PaymentMethod')

        selected_project = get_object_or_404(
            projects,
            id=request.POST.get('Project')
        )

        payment.Project = selected_project
        payment.save()

        return redirect('payments')

    return render(request, 'update_payments.html', {
        'payment': payment,
        'projects': all_projects
    })

def delete_payment(request, id):
    if request.method == 'POST':
        payment = get_object_or_404(payments, id=id)
        payment.delete()

    return redirect('payments')

def projectassignment_view(request):

    if request.method == 'POST':

        selected_employee = employees.objects.get(
            id=request.POST.get('Employee')
        )

        selected_project = projects.objects.get(
            id=request.POST.get('Project')
        )

        projectassignment.objects.create(
            Employee=selected_employee,
            Project=selected_project,
            AssignmentRole=request.POST.get('AssignmentRole'),
            AssignmentDate=request.POST.get('AssignmentDate')
        )

        return redirect('projectassignment')

    all_assignments = projectassignment.objects.all()
    all_employees = employees.objects.all()
    all_projects = projects.objects.all()

    return render(request, 'projectassignment.html', {
        'assignments': all_assignments,
        'employees': all_employees,
        'projects': all_projects
    })

def update_projectassignment(request, id):
    assignment = get_object_or_404(projectassignment, id=id)

    all_employees = employees.objects.all()
    all_projects = projects.objects.all()

    if request.method == 'POST':
        assignment.AssignmentRole = request.POST.get('AssignmentRole')
        assignment.AssignmentDate = request.POST.get('AssignmentDate')

        selected_employee = get_object_or_404(
            employees,
            id=request.POST.get('Employee')
        )

        selected_project = get_object_or_404(
            projects,
            id=request.POST.get('Project')
        )

        assignment.Employee = selected_employee
        assignment.Project = selected_project

        assignment.save()

        return redirect('projectassignment')

    return render(request, 'update_projectassignment.html', {
        'assignment': assignment,
        'employees': all_employees,
        'projects': all_projects
    })

def delete_projectassignment(request, id):
    if request.method == 'POST':
        assignment = get_object_or_404(projectassignment, id=id)
        assignment.delete()

    return redirect('projectassignment')


