from django.contrib import admin
from .models import (
    clients,
    department,
    employees,
    projects,
    supplier,
    materials,
    payments,
    projectassignment
)

# Register your models here.

admin.site.register(clients)
admin.site.register(department)
admin.site.register(employees)
admin.site.register(projects)
admin.site.register(supplier)
admin.site.register(materials)
admin.site.register(payments)
admin.site.register(projectassignment)

