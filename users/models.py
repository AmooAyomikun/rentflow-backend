from django.db import models

# Create your models here.
class Tenant(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default='tenant')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


