import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis keyspace hits, misses, and hit ratio.
    """
    redis_conn = get_redis_connection("default")  # Use the default Django cache alias
    info = redis_conn.info("stats")  # Get Redis stats
    
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0.0
    
    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio
    }
    
    logger.info(f"Redis cache metrics: {metrics}")
    
    return metrics

