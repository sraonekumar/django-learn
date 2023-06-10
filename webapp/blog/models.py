from django.db import models
import datetime
# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=12)
    total_cost = models.IntegerField()