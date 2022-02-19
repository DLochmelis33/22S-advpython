import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


# Насколько я понял, чтобы звать нумпаевские функции, необходимо
# приводить внутренности своего класса к np.ndarray, потому что
# сами реализации все равно будут только там.

# А если так, то домашка делается копипастом примера из файла
# numpy.lib.mixins.NDArrayOperatorsMixin, и никак иначе.


class MyStrMixin:
    def __str__(self):
        res = ""
        for row in self._data:
            res += str(row) + "\n"
        return res


class MyGetSetMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d):
        self._data = np.asarray(d)


class MyFileMixin:
    def to_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write(self._data.__repr__())


class MyMixinMatrix(NDArrayOperatorsMixin, MyStrMixin, MyGetSetMixin, MyFileMixin):
    def __init__(self, value):
        self._data = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, )

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use MyMixinMatrix instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle MyMixinMatrix objects.
            if not isinstance(x, self._HANDLED_TYPES + (MyMixinMatrix,)):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x._data if isinstance(x, MyMixinMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x._data if isinstance(x, MyMixinMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)
