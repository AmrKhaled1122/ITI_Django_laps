from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.name} ({self.email})"
