from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
from restaurant.models import Restaurant

class Review(models.Model):
    """
    Model to represent a review of a restaurant by a user.

    Fields:
        user (ForeignKey): The user who wrote the review.
        restaurant (ForeignKey): The restaurant being reviewed.
        rating (PositiveIntegerField): The rating given by the user (1 to 5).
        review_text (TextField): The text of the review.
        visit_date (DateField): The date of the visit to the restaurant.

    Methods:
        save(): Overrides the save method to update the restaurant's average rating after saving a review.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()
    visit_date = models.DateField()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the restaurant's average rating after saving a review.
        """
        super().save(*args, **kwargs)
        self.restaurant.update_rating()
