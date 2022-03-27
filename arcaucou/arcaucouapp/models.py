from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Date is added automatically
    date = models.DateField(auto_now_add=True)
    # Time in milliseconds
    time = models.DecimalField(max_digits=10, decimal_places=0)
    
class Group(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class UserToGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)