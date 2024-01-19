from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.TextField(null=True, blank=True)
    M,F = 'Male', 'Female'
    sex_choices = [(M, 'Male'), (F, 'Female')]
    sex = models.CharField(
        max_length=10,
        choices=sex_choices,
        null=True, blank=True
    )
    
    def __str__(self):
        return f'Name: {self.name}, sex: {self.sex}'

class Location(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    place_name = models.TextField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    
