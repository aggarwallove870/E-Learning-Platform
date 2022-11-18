from django.db import models
# Create your models here.

Roles_choice = (
    ("Employees", "Employees"),
    ("Manager", "Manager"),
)
class CreateOrigination(models.Model):

    origination = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    roles = models.CharField(max_length=9,
                choices=Roles_choice,
                default="Employees")
    
    def __str__(self):
        return self.origination






