from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
class Group(models.Model):
    name = models.CharField(max_length=255)
    
class UserToGroup(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
class Leaderboard(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Date is added automatically
    date = models.DateField(auto_now_add=True)
    # Time in milliseconds
    time = models.DecimalField(max_digits=10, decimal_places=0)