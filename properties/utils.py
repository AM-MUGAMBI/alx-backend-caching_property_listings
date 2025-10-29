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
