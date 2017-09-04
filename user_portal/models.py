from django.db import models

# Create your models here.

class EndUsers(models.Model):
    user_id = models.CharField(max_length=20,unique=True,default='U_test',primary_key=True)
    username = models.CharField(max_length=20,default='U_Name')
    password = models.CharField(max_length=20)
    email = models.CharField(max_length = 50)
    def __str__(self):
        return self.username
