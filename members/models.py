from django.db import models

# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    
    def __str__(self) -> str:
        return f"{self.fullname} {self.email}"