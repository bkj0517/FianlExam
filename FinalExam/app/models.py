from django.db import models

# Create your models here.

class Menu(models.Model):
    menuname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.menuname
