from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    is_librarian = models.BooleanField(default=False)
    
    def clean_phone(self):
        if User.objects.filter(phone=self.phone).exists():
            raise ValidationError("Phone number already exists")
    
    def __str__(self):
        return self.full_name