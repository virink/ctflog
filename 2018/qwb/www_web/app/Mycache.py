import os
import errno
import tempfile
from hashlib import md5
from time import time
from others import load
from cPickle import dump, PickleError
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle
'''
from werkzeug._compat import iteritems, text_type
from werkzeug.posixemulation import rename


def _items(mappings):
    if hasattr(mappings, 'items'):
        return iteritems(mappings)
    return mappings


class BaseCache(object):

    def __init__(self, default_timeout=300):
        self.default_timeout = default_timeout

    def _normalize_timeout(self, timeout):
        if timeout is None:
            timeout = self.default_timeout
        return timeout

    def get(self, key):
        return None

    def delete(self, key):
        return True

    def get_many(self, *keys):
        return map(self.get, keys)

    def get_dict(self, *keys):
        return dict(zip(keys, self.get_many(*keys)))

    def set(self, key, value, timeout=None):
        return True

    def add(self, key, value, timeout=None):
        return True

    def set_many(self, mapping, timeout=None):
        rv = True
        for key, value in _items(mapping):
            if not self.set(key, value, timeout):
                rv = False
        return rv

    def delete_many(self, *keys):
        return all(self.delete(key) for key in keys)

    def has(self, key):
        raise NotImplementedError(
            '%s doesn\'t have an efficient implementation of `has`. That '
            'means it is impossible to check whether a key exists without '
            'fully loading the key\'s data. Consider using `self.get` '
            'explicitly if you don\'t care about performance.'
        )

    def clear(self):
        return True

    def inc(self, key, delta=1):
        value = (self.get(key) or 0) + delta
        return value if self.set(key, value) else None

    def dec(self, key, delta=1):
        value = (self.get(key) or 0) - delta
        return value if self.set(key, value) else None


class FileSystemCache(BaseCache):
    _fs_transaction_suffix = '.cache'

    def __init__(self, cache_dir, threshold=500, default_timeout=300,
                 mode=0o600):
        print("FileSystemCache init")
        print(cache_dir)
        BaseCache.__init__(self, default_timeout)
        self._path = cache_dir
        self._threshold = threshold
        self._mode = mode

        try:
            os.makedirs(self._path)
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

    def _normalize_timeout(self, timeout):
        timeout = BaseCache._normalize_timeout(self, timeout)
        if timeout != 0:
            timeout = time() + timeout
        return int(timeout)

    def _list_dir(self):
        return [os.path.join(self._path, fn) for fn in os.listdir(self._path)
                if not fn.endswith(self._fs_transaction_suffix)]

    def _prune(self):
        entries = self._list_dir()
        if len(entries) > self._threshold:
            now = time()
            for idx, fname in enumerate(entries):
                try:
                    remove = False
                    with open(fname, 'rb') as f:
                        expires = load(f)
                    remove = (expires != 0 and expires <= now) or idx % 3 == 0

                    if remove:
                        os.remove(fname)
                except (IOError, OSError):
                    pass

    def clear(self):
        for fname in self._list_dir():
            try:
                os.remove(fname)
            except (IOError, OSError):
                return False
        return True

    def _get_filename(self, key):
        if isinstance(key, text_type):
            key = key.encode('utf-8')  # XXX unicode review
        hash = md5(key).hexdigest()
        return os.path.join(self._path, hash)

    def get(self, key):
        filename = self._get_filename(key)
        try:
            with open(filename, 'rb') as f:
                pickle_time = load(f)
                if pickle_time == 0 or pickle_time >= time():
                    a = load(f)
                    return a
                else:
                    os.remove(filename)
                    return None
        except (IOError, OSError, PickleError):
            return None

    def add(self, key, value, timeout=None):
        filename = self._get_filename(key)
        if not os.path.exists(filename):
            return self.set(key, value, timeout)
        return False

    def set(self, key, value, timeout=None):
        timeout = self._normalize_timeout(timeout)
        filename = self._get_filename(key)
        self._prune()
        try:
            fd, tmp = tempfile.mkstemp(suffix=self._fs_transaction_suffix,
                                       dir=self._path)
            with os.fdopen(fd, 'wb') as f:
                dump(timeout, f, 1)
                dump(value, f, 2)
            rename(tmp, filename)
            os.chmod(filename, self._mode)
        except (IOError, OSError):
            return False
        else:
            return True

    def delete(self, key):
        try:
            os.remove(self._get_filename(key))
        except (IOError, OSError):
            return False
        else:
            return True

    def has(self, key):
        filename = self._get_filename(key)
        try:
            with open(filename, 'rb') as f:
                pickle_time = load(f)
                if pickle_time == 0 or pickle_time >= time():
                    return True
                else:
                    os.remove(filename)
                    return False
        except (IOError, OSError, PickleError):
            return False
