from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
# when you create app then flow 
# register app (setting.py)
# create Model () -> makemigrations -> migrate
# make urls -> then views
# 