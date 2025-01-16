from django.db import models

# Create your models here.

class department(models.Model):
    id=models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=150)

    def __str__(self):
        return self.dept_name
    
    class Meta:
        db_table='department'

class studentData(models.Model):
    gender=[
        ('male', 'Male'),
        ('female', 'Female')
    ]

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    rollno=models.IntegerField(unique=True)
    gender=models.CharField(choices=gender)
    place=models.CharField(max_length=150)
    fees_amt=models.IntegerField()
    department=models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='student_table'