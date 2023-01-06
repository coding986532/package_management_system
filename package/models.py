from django.db import models

# Create your models here.

class Installer(models.Model):
    Name = models.CharField(max_length=300)
    Date_Added = models.DateField()
    Installer_Link = models.CharField(max_length=2083)
    App_Developer_Website = models.CharField(max_length=2083)