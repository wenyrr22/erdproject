from django.db import models

class Task(models.Model):
    title = models.CharField(unique=True, max_length=200, verbose_name="название задачи")
    description=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.title

