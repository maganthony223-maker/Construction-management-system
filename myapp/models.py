from django.db import models

# Create your models here.

class clients(models.Model):
    Full_Name = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(unique=True)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.Full_Name


class department(models.Model):
    Department_Name = models.CharField(max_length=100)
    Office_Location = models.CharField(max_length=100)

    def __str__(self):
        return self.Department_Name

class employees(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=20)
    Position = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=12, decimal_places=2)
    Hire_Date = models.DateField()
    Department = models.ForeignKey(
        department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.FirstName + " " + self.LastName

class projects(models.Model):
    ProjectName = models.CharField(max_length=150)
    Location = models.CharField(max_length=150)
    Budget = models.DecimalField(max_digits=15, decimal_places=2)
    Status = models.CharField(max_length=50)
    Client = models.ForeignKey(
        clients,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.ProjectName



class supplier(models.Model):
    SupplierName = models.CharField(max_length=150)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.SupplierName


class materials(models.Model):
    MaterialName = models.CharField(max_length=150)
    UnitPrice = models.DecimalField(max_digits=12, decimal_places=2)
    QuantityInStock = models.IntegerField()
    Supplier = models.ForeignKey(
        supplier,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.MaterialName



class payments(models.Model):
    Project = models.ForeignKey(
        projects,
        on_delete=models.CASCADE
    )
    AmountPaid = models.DecimalField(max_digits=15, decimal_places=2)
    PaymentDate = models.DateField()
    PaymentMethod = models.CharField(max_length=50)

    def __str__(self):
        return str(self.AmountPaid)



class projectassignment(models.Model):
    Employee = models.ForeignKey(
        employees,
        on_delete=models.CASCADE
    )
    Project = models.ForeignKey(
        projects,
        on_delete=models.CASCADE
    )
    AssignmentRole = models.CharField(max_length=100)
    AssignmentDate = models.DateField()

    def __str__(self):
        return self.AssignmentRole
