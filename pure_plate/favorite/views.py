from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Favorite
from restaurant.models import Restaurant
from account.models import User

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorites(request, restaurant_name):
    """
    Add a restaurant to the user's favorites.

    Args:
        request: The HTTP request object.
        restaurant_name: The name of the restaurant to add to favorites.

    Returns:
        HTTP 201 Created if the restaurant is successfully added to favorites.
        HTTP 200 OK if the restaurant is already in favorites.
        HTTP 404 Not Found if the restaurant does not exist.
    """
    user = request.user
    try:
        restaurant = Restaurant.objects.get(name=restaurant_name)
        favorite, created = Favorite.objects.get_or_create(user=user, restaurant=restaurant)
        if created:
            return Response({'message': 'Restaurant added to favorites successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Restaurant is already in favorites'}, status=status.HTTP_200_OK)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorites(request):
    """
    Retrieve the list of the user's favorite restaurants.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP 200 OK with the list of favorite restaurants.
    """
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    favorite_restaurants = [{'restaurant_id': favorite.restaurant.id, 'restaurant_name': favorite.restaurant.name} for favorite in favorites]
    return Response({'favorites': favorite_restaurants}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_favorites(request, restaurant_name):
    """
    Remove a restaurant from the user's favorites.

    Args:
        request: The HTTP request object.
        restaurant_name: The name of the restaurant to remove from favorites.

    Returns:
        HTTP 200 OK if the restaurant is successfully removed from favorites.
        HTTP 404 Not Found if the restaurant is not in favorites or does not exist.
    """
    user = request.user
    try:
        restaurant = Restaurant.objects.get(name=restaurant_name)
        favorite = Favorite.objects.filter(user=user, restaurant=restaurant)
        if favorite.exists():
            favorite.delete()
            return Response({'message': 'Restaurant removed from favorites successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Restaurant is not in favorites'}, status=status.HTTP_404_NOT_FOUND)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
