import os
import diskcache
import hashlib
import time
from .common import logger


def wait_key(cache, key, timeout=30, delete=True):
    t = time.time()
    while True:
        result = cache.get(key)
        if result:
            if delete:
                cache.delete(key)
            return result
        if time.time() - t > timeout:
            raise ValueError('Remote request timed out')
        time.sleep(0.5)


class NullCache:
    def get(self, key):
        return None

    def set(self, key, value, ttl=3600):
        return value

    def delete(self, key):
        pass

    def wait_key(self, key, timeout=30, delete=True):
        raise NotImplementedError(
            "This function is not available without a cache")


class FileCache(NullCache):
    def __init__(self, path):
        self.cache = diskcache.Cache(path)

    def _key(self, data):
        h = hashlib.sha1()
        h.update(repr(data).encode('utf-8'))
        return h.hexdigest()

    def get(self, key):
        return self.cache.get(self._key(key))

    def set(self, key, value, ttl=3600):
        self.cache.set(self._key(key), value, expire=ttl)
        return value

    def delete(self, key):
        self.cache.delete(self._key(key))

    def wait_key(self, key, timeout=30, delete=True):
        return wait_key(self, key, timeout, delete)


if 'FILE_CACHE' in os.environ:
    cache = FileCache(os.environ['FILE_CACHE'])
else:
    logger.warning(
        'Using NullCache, some features like remote requests will not work')
    cache = NullCache()


def get_cache():
    return cache


def set_cache(cache):
    """Set the caching options. It is recommended to
    set the caching via environment variables.

    Currently only `FileCache` is available:
    `FILE_CACHE=/path/to/cache`

    Default is that no cache will be used.
    """
    globals['cache'] = cache
