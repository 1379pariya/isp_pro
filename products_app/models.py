from django.db import models
from accounts_app.models import seller , costumer

class product(models.Model):
     name = models.CharField(max_length=100)
     seller = models.ForeignKey(seller, on_delete=models.CASCADE)
     costumer = models.ManyToManyField(costumer)
     price = models.IntegerField()
     description = models.TextField(null=True, blank=True)
     def __str__(self):
        return self.name


    
