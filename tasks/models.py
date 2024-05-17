from django.db import models
from projects.models import Project

# Create your models here.
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_id = models.AutoField(primary_key=True)
    task_description = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.task_id:
            # Get the maximum task_id for the current project
            max_task_id = Task.objects.filter(project=self.project).aggregate(models.Max('task_id'))['task_id__max']
            self.task_id = (max_task_id or 0) + 1
        super().save(*args, **kwargs)