from django.http import JsonResponse
from django.db.models import Count
from .models import Restaurant, Category

def restaurants_list(request):

    try:
        restaurants = Restaurant.objects.all()
        
        data = [{
            'Id': restaurant.id,
            'Name': restaurant.name,
            'Address': restaurant.address,
            'Latitude': str(restaurant.latitude),
            'Longitude': str(restaurant.longitude),
            'Time': restaurant.time,
            'Photo': restaurant.photo,
            'Phone': restaurant.phone,
            'ReviewCount': restaurant.review_count,
            'Rating': str(restaurant.avg_rating),
            'Vegan': restaurant.vegan,
            'Halal': restaurant.halal,
            'GlutenFree': restaurant.gluten_free,
            'LactoFree': restaurant.lacto_free
        } for restaurant in restaurants]

        # filtered restaurants list category by category
        data = {}
        for category_name in category_names_list:
            category_restaurants = restaurants.filter(categories__CategoryName=category_name)
            category_list = [{
                'restaurantId': restaurant.id,
                'restaurantName': restaurant.name,
                'restaurantAddress': restaurant.address,
                'restaurantLatitude': float(restaurant.latitude),
                'restaurantLongitude': float(restaurant.longitude),
                # 'restaurantTime': restaurant.time,
                # 'restaurantPhoto': restaurant.photo,
                # 'restaurantPhone': restaurant.phone,
                'restaurantReviewCount': restaurant.review_count,
                'restaurantRating': str(restaurant.avg_rating),
            } for restaurant in category_restaurants]
            data[f"{category_name}List"] = category_list

        response = {
            'status': 200,
            'message': 'Successfully retrieved the restaurant list.',
            'data': data
        }

        return JsonResponse(response, status=200)

    except Exception as e:
        return JsonResponse({'status': 400, 'message': str(e), 'data': []}, status=400)



