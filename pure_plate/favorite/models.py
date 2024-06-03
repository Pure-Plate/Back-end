from django.db import models
from account.models import User
from restaurant.models import Restaurant

class Favorite(models.Model):
    """
    Model to represent a user's favorite restaurant.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'restaurant')  # Ensure each user-restaurant pair is unique
