from django.db import models

# Create your models here.       F H I M 
class Department(models.Model):
    DEPT_CHOICES = [
        ('Finance - Pune', 'Finance-Pune'),
        ('Finance - Begaluru', 'Finance - Bengaluru'),
        ('HR - Pune', 'HR - Pune'),
        ('HR - Bengaluru', 'HR - Bengaluru'),
        ('IT - Pune', 'IT-Pune'),
        ('IT - Begaluru', 'IT - Bengaluru'),
        ('Marketing - Pune', 'Marketing-Pune'),
        ('Marketing - Begaluru', 'Marketing - Bengaluru')]
    
    name = models.CharField(max_length=50, choices=DEPT_CHOICES)

    def __str__(self):
        return self.name

class Role(models.Model):
    ROLE_CHOICES = [
        ('Analyst', 'Analyst'),
        ('Data Analyst', 'Data Analyst'),
        ('HR Manager', 'HR Manager'),
        ('Software Engineer', 'Software Engineer'),
        ('Python Developer', 'Python Developer'),
        ('Sales Executive', 'Sales Executive'),
        ('Java Developer', 'Java Developer'),
        ('Intern', 'Intern'),
        ('Sales Executive', 'Sales Executive'),
        ('SQL Developer', 'SQL Developer'),
        ('Project Manager', 'Project Manager')]
    name = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name   

class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    salary = models.IntegerField(default = 0)
    phone = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

