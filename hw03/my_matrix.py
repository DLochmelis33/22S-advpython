from typing import List, Any
from functools import lru_cache
from mixin_matrix import MyStrMixin


class MyMatrixException(Exception):
    pass


# обыкновенный полиномиальный хеш
class MyHashMixin:
    _P = 13
    _R = 1009  # небольшой модуль, чтобы найти коллизию

    def __hash__(self):
        res = 0
        for row in self._data:
            for elem in row:
                res = (res * self._P + elem) % self._R
        return int(res)  # in case `elem` is not int


class MyMatrix(MyHashMixin, MyStrMixin):

    def __init__(self, data: List[List[Any]]):
        if len(data) == 0:
            raise MyMatrixException("empty data is not allowed")
        for (l1, l2) in zip(data, data[1:]):
            if len(l1) != len(l2):
                raise MyMatrixException("not rectangle data")
            if len(l1) == 0:
                raise MyMatrixException("empty row is not allowed")
        self._data = data
        self._h = len(data)
        self._w = len(data[0])

    def __add__(self, other):
        if not isinstance(other, MyMatrix):
            raise MyMatrixException("addition only allowed on two MyMatrix objects")
        if self._h != other._h or self._w != other._w:
            raise MyMatrixException("dimensions do not match")
        result = []
        for i in range(self._w):
            result.append([])
            for j in range(self._h):
                result[-1].append(self._data[i][j] + other._data[i][j])
        return MyMatrix(result)

    def __mul__(self, other):
        # copy-paste :)
        if not isinstance(other, MyMatrix):
            raise MyMatrixException("element-wise multiplication only allowed on two MyMatrix objects")
        if self._h != other._h or self._w != other._w:
            raise MyMatrixException("dimensions do not match")
        result = []
        for i in range(self._w):
            result.append([])
            for j in range(self._h):
                result[-1].append(self._data[i][j] * other._data[i][j])
        return MyMatrix(result)

    @lru_cache(maxsize=10)
    def __matmul__(self, other, default_element=0):
        if not isinstance(other, MyMatrix):
            raise MyMatrixException("matrix multiplication only allowed on two MyMatrix objects")
        if self._w != other._h:
            raise MyMatrixException("dimensions do not match")
        result = []
        for i in range(self._h):
            result.append([])
            for j in range(other._w):
                tmp = default_element
                for k in range(self._w):
                    tmp += self._data[i][k] * other._data[k][j]
                result[-1].append(tmp)
        return MyMatrix(result)
