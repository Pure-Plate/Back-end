from django.db import models
from django.db.models import Avg

class Restaurant(models.Model):
    """
    Model to represent a restaurant.

    Fields:
        name (CharField): The name of the restaurant.
        address (CharField): The address of the restaurant.
        latitude (DecimalField): The latitude coordinate of the restaurant.
        longitude (DecimalField): The longitude coordinate of the restaurant.
        time (CharField): The operating time of the restaurant.
        photo (CharField): The URL of the restaurant's photo.
        phone (CharField): The contact phone number of the restaurant.
        review_count (IntegerField): The total number of reviews for the restaurant.
        avg_rating (DecimalField): The average rating of the restaurant.
        vegan (BooleanField): Indicates if the restaurant offers vegan options.
        halal (BooleanField): Indicates if the restaurant offers halal options.
        gluten_free (BooleanField): Indicates if the restaurant offers gluten-free options.
        lacto_free (BooleanField): Indicates if the restaurant offers lactose-free options.

    Methods:
        update_rating(): Updates the review count and average rating of the restaurant.
    """

    name = models.CharField(max_length=255, db_index=True)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    time = models.CharField(max_length=255, db_index=True)
    photo = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=255, db_index=True)
    review_count = models.IntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    vegan = models.BooleanField(default=False)
    halal = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    lacto_free = models.BooleanField(default=False)

    def update_rating(self):
        """
        Updates the review count and average rating of the restaurant.
        """
        self.review_count = self.review_set.count()
        if self.review_count > 0:
            self.avg_rating = self.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
        else:
            self.avg_rating = 0.00
        self.save()
