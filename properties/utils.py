from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Check if data exists in cache
    properties = cache.get('all_properties')
    
    if properties is None:
        print("Cache miss — fetching from database")
        # Fetch from DB and convert to list of dicts
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        ))
        # Store in Redis cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    else:
        print("Cache hit — loading from Redis")
    
    return properties

