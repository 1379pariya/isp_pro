from django.db import models

class seller(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    is_confirm=models.BooleanField(default=False)
    def __str__(self):
        return self.name



class costumer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    wallet=models.IntegerField(default=0)
    is_confirm=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    


