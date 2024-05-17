from django.db import models

# Create your models here.
class Project(models.Model):
    project_code = models.CharField(max_length=50, primary_key=True)
    project_name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.project_code} {self.project_name}"