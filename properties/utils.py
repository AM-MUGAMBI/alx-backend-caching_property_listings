from django_redis import get_redis_connection

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit ratio.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total_requests = hits + misses
    hit_ratio = hits / total_requests if total_requests > 0 else 0

    # Log metrics using print instead of logger
    print(f"Redis Cache Metrics - Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")

    return hit_ratio
