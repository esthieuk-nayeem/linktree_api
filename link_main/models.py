from django.db import models
from authentication.models import User
# Create your models here.

class LinkModel(models.Model):
    title = models.CharField(null=False, max_length=250)
    link = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    prioritize = models.BooleanField(default=False)
    lock = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

