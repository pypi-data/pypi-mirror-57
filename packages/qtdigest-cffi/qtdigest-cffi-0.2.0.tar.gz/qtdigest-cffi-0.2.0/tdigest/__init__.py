from collections import namedtuple
from threading import Lock
from ._tdigest import lib as _lib

DEFAULT_COMPRESSION = 400

Centroid = namedtuple("Centroid", ("weight", "mean"))


class RawTDigest(object):
    def __init__(self, compression=DEFAULT_COMPRESSION):
        if not isinstance(compression, int):
            raise TypeError("'compression' must be of type 'int'")

        if compression <= 0:
            raise ValueError("'compression' must larger than 0")

        self._struct = _lib.tdigest_new(compression)

    def __del__(self):
        if hasattr(self, "_struct"):
            _lib.tdigest_free(self._struct)

    def _compress(self):
        _lib.tdigest_compress(self._struct)

    @property
    def compression(self):
        return self._struct.compression

    @property
    def threshold(self):
        return self._struct.threshold

    @property
    def size(self):
        return self._struct.size

    @property
    def weight(self):
        if self._struct.point_count:
            self._compress()

        return self._struct.weight

    @property
    def centroid_count(self):
        if self._struct.point_count:
            self._compress()

        return self._struct.centroid_count

    @property
    def compression_count(self):
        return self._struct.compression_count

    def push(self, value, weight=1):
        if not isinstance(value, (float, int)):
            raise TypeError("'value' must be of type 'float' or 'int'")

        if not isinstance(weight, int):
            raise TypeError("'weight' must be of type 'int'")

        if weight <= 0:
            raise ValueError("'weight' must larger than 0")

        _lib.tdigest_add(self._struct, value, weight)

    def quantile(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("'value' must be of type 'float'")

        if value < 0.0 or value > 1.0:
            raise ValueError("'value' must be between 0.00 and 1.00")

        return _lib.tdigest_quantile(self._struct, value)

    def percentile(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'value' must be of type 'float' or 'int'")

        if value < 0 or value > 100:
            raise ValueError("'value' must be between 0 and 100")

        return _lib.tdigest_quantile(self._struct, value / 100)

    def cdf(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'value' must be of type 'float' or 'int'")

        return _lib.tdigest_cdf(self._struct, value)

    def centroids(self):
        for i in range(self.centroid_count):
            centroid = self._struct.centroids[i]
            yield Centroid(centroid.weight, centroid.mean)

    def merge(self, other):
        if not isinstance(other, (TDigest, RawTDigest)):
            raise TypeError("'value' must be of type 'TDigest' or 'RawTDigest'")

        _lib.tdigest_merge(self._struct, other._struct)

    def simpleSerialize(self):
        if self.size == 0:
            return ''
        self._compress()
        result = []
        for c in self.centroids():
            result.append(str(c.mean))
            result.append(str(c.weight))
        return '~'.join(result)


class TDigest(RawTDigest):
    def __init__(self, compression=DEFAULT_COMPRESSION):
        super(TDigest, self).__init__(compression)
        self._lock = Lock()

    @property
    def compression(self):
        with self._lock:
            return super(TDigest, self).compression

    @property
    def threshold(self):
        with self._lock:
            return super(TDigest, self).threshold

    @property
    def size(self):
        with self._lock:
            return super(TDigest, self).size

    @property
    def weight(self):
        with self._lock:
            return super(TDigest, self).weight

    @property
    def centroid_count(self):
        with self._lock:
            return super(TDigest, self).centroid_count

    @property
    def compression_count(self):
        with self._lock:
            return super(TDigest, self).compression_count

    def push(self, value, weight=1):
        with self._lock:
            return super(TDigest, self).push(value, weight)

    def quantile(self, value):
        with self._lock:
            return super(TDigest, self).quantile(value)

    def percentile(self, value):
        with self._lock:
            return super(TDigest, self).percentile(value)

    def cdf(self, value):
        with self._lock:
            return super(TDigest, self).cdf(value)

    def centroids(self):
        with self._lock:
            return super(TDigest, self).centroids()

    def merge(self, other):
        with self._lock:
            return super(TDigest, self).merge(other)
