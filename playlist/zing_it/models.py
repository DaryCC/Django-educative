from datetime import date
from django.db import models
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=264, unique=True)
    number_of_employees = models.IntegerField(blank=True, null=True,default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):

    employee_name = models.CharField(max_length=264, unique= True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default= date.today)

    def __str__(self):
        return self.employee_name


class Project(models.Model):

    project_name = models.CharField(max_length=264, unique= True,primary_key=True)
    employee_name = models.ManyToManyField('Employee')
    team_lead = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='team_lead',null=True)


    def __str__(self):
        return self.project_name
