from django.db import models
from account.models import User
from project.models import Project
import uuid
# Create your models here.
class Todolist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todolists')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolists')

    def __str__(self):
        return self.name
