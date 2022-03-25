from django.db import models
from datetime import date

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True,help_text="Escribe nombre del tema")

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE,help_text="Escribe el nombre de la página.")
    name = models.CharField(max_length=264, unique= True)
    url = models.URLField(unique= True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete= models.CASCADE)
    date = models.DateField(default= date.today)
    count = models.IntegerField(default=0)
    prueba = models.IntegerField(default=222)
    def __str__(self):
        return str(self.date)

# aqui empieza el otro modelo
class Company(models.Model):
    name = models.CharField(max_length=264,unique=True)
    number_of_employees= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):

    employee_name = models.CharField(max_length=264, unique= True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default= date.today,help_text="yyyy/mm/dd")

    def __str__(self):
        return self.employee_name

class Projects (models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    employee_name = models.ManyToManyField(Employee)
    team_lead = models.OneToOneField('Employee',on_delete=models.CASCADE, related_name="team_lead_reverse",default="alguna_mamada")
    def __str__(self):
        return  self.project_name
