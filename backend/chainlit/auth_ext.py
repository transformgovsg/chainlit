import cachetools
from chainlit.config import config
from chainlit.logger import logger

# This blacklist blocks out JWT Tokens when users click "Log out" / "Sign out" manually
jwt_blacklist = cachetools.TTLCache(
    maxsize=8096, ttl=config.project.user_session_timeout
)

users_jwt_cache = cachetools.TTLCache(
    maxsize=8096, ttl=config.project.user_session_timeout
)


def remove_from_cache(cache, key):
    """
    Remove an item from the specified cache using the key.

    :param cache: The cache object (either jwt_blacklist or users_jwt_cache)
    :param key: The key to remove from the cache
    """
    try:
        del cache[key]
    except KeyError:
        logger.warning(f"Failed to remove non-existent key '{key}' from cache.")
        pass
