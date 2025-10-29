from django_redis import get_redis_connection

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit ratio.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    hit_ratio = hits / (hits + misses)  # calculates hit ratio directly

    return hit_ratio
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        ))
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    hit_ratio = hits / (hits + misses)  # simple calculation

    logger.info(f"Redis cache hits: {hits}, misses: {misses}, hit ratio: {hit_ratio:.2f}")
    return hit_ratio
