from django.db import models

# Create your models here.
class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="my models"
        db_table='Department'
        ordering=['name']

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    email=models.EmailField()
    phone = models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    bonus=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name