from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)  # input
    content = models.TextField()  # textarea
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

