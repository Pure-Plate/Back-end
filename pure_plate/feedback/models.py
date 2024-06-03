from django.db import models
from restaurant.models import Restaurant

class Feedback(models.Model):
    """
    Model to represent feedback for a restaurant.
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='feedbacks')
    vegan = models.BooleanField(blank=True, null=True)  # Indicates if the restaurant offers vegan options
    halal = models.BooleanField(blank=True, null=True)  # Indicates if the restaurant offers halal options
    gluten_free = models.BooleanField(blank=True, null=True)  # Indicates if the restaurant offers gluten-free options
    lacto_free = models.BooleanField(blank=True, null=True)  # Indicates if the restaurant offers lactose-free options
    comments = models.TextField(blank=True, null=True)  # Additional comments about the restaurant

    def __str__(self):
        """
        Return a string representation of the feedback.
        """
        return f"Feedback for {self.restaurant.name}"
