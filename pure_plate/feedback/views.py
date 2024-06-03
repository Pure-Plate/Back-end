import json

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Restaurant, Feedback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def createFeedback(request):
    """
    API view to handle the creation of feedback for a restaurant.

    Args:
        request: The HTTP request object containing the feedback data.

    Returns:
        JsonResponse: A response indicating success or failure of feedback submission.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the JSON request body
        except ValueError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)  # Return error if JSON is invalid
        
        restaurant_name = data.get('restaurant_name')  # Get the restaurant name from the request data
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)  # Retrieve the restaurant object
        
        # Create the feedback object
        Feedback.objects.create(
            restaurant=restaurant,
            vegan=data.get('vegan') == 'true',
            halal=data.get('halal') == 'true',
            gluten_free=data.get('gluten_free') == 'true',
            lacto_free=data.get('lacto_free') == 'true',
            comments=data.get('comments')
        )

        return JsonResponse({'message': 'Feedback submitted successfully'}, status=201)  # Return success response
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)  # Return error for unsupported HTTP methods
