from django.db import models
import django.utils.timezone as tm

def withID(self, string):
    return string + ' (' + str(self.id) + ')'

max_length_basic = 100

class Company(models.Model):
    name = models.CharField(max_length=max_length_basic)
    address = models.CharField(max_length=max_length_basic)
    country = models.CharField(max_length=max_length_basic)

    def __str__(self):
        return withID(self, self.name)

class Person(models.Model):
    first_name = models.CharField(max_length=max_length_basic)
    last_name = models.CharField(max_length=max_length_basic)

    def __str__(self):
        return withID(self, self.first_name + ' ' + self.last_name)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    hiring_date = models.DateTimeField('date hired', default=tm.now)

    def __str__(self):
        return str(self.person) + ' at ' + str(self.company)

    # j'ai essayé sans succès de faire du couple (company, person) un couple unique à chaque employé
    # en conséquence une entreprise peut embaucher plusieurs fois en même temps quelqu'un

# Create your models here.
