import json

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import User, Restaurant, Review

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def review(request):
    """
    View function to create a new review.

    Accepts POST requests with JSON data containing information about the review.
    Validates the data and creates a new review in the database.

    Returns:
        JsonResponse: JSON response indicating success or failure of the review creation.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except ValueError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        user_id = data.get('user_id')
        restaurant_id = data.get('restaurant_id')
        rating = data.get('rating')
        review_text = data.get('review_text')
        visit_date = data.get('visit_date')

        # Validation
        if not all([user_id, restaurant_id, rating, review_text, visit_date]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return JsonResponse({'error': 'Rating must be an integer between 1 and 5'}, status=400)

        try:
            # Validate existence
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, Restaurant.DoesNotExist):
            return JsonResponse({'error': 'User or restaurant not found'}, status=404)

        review = Review.objects.create(
            user=user,
            restaurant_id=restaurant_id,
            rating=rating,
            review_text=review_text,
            visit_date=visit_date
        )

        return JsonResponse({'message': 'Review created successfully'}, status=201)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def reviews_list(request):
    """
    View function to retrieve a list of reviews for a restaurant.

    Accepts GET requests with the restaurant name as a query parameter.
    Retrieves reviews for the specified restaurant and returns them as JSON.

    Returns:
        JsonResponse: JSON response containing a list of reviews for the restaurant.
    """
    if request.method == 'GET':
        restaurant_name = request.GET.get('name')
        
        if not restaurant_name:
            return JsonResponse({'error': 'Restaurant name is required'}, status=400)

        # Get the restaurant by name
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)
        
        # Get reviews for the restaurant
        reviews = Review.objects.filter(restaurant=restaurant)
        
        # Prepare the review data
        review_list = [{
            'review_id': review.id,
            'user_id': review.user.id,
            'user_name': review.user.username, 
            'rating': review.rating,
            'review_text': review.review_text,
            'visit_date': review.visit_date,
        } for review in reviews]
        
        return JsonResponse({'reviews': review_list}, status=200)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
