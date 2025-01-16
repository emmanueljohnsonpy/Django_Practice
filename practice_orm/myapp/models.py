from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date_joined=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_date=models.DateField()
    isbn=models.CharField(max_length=13, unique=True)
    pages=models.IntegerField()
    status=models.CharField(max_length=20, choices=[('available', 'Available'), ('checked_out', 'Checked_Out')])

    def __str__(self):
        return self.title
    
class Car(models.Model):
    owner=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    buyed_year=models.IntegerField()
    manufacturer=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.color} {self.manufacturer} {self.model} ({self.buyed_year}) owned by {self.owner}"
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Bike(models.Model):
    make=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField()
    owner=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
    
class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name    

""" class CommonInfo(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        abstract=True

class Student(CommonInfo):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

class Teacher(CommonInfo):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=50) """

class Person1(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()

class Student1(Person1):
    enrollment_date=models.DateField()
    major=models.CharField(max_length=50)

class Teacher1(Person1):
    hire_date=models.DateField()
    subject=models.CharField(max_length=50)

    