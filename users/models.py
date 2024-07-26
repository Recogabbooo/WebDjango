from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# OnetoOneField()

class Cliente(User):
    class Meta:
        proxy = True
        
    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    biografia = models.TextField()