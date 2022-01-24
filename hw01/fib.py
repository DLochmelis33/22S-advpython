from typing import List


def fib(n: int) -> List[int]:
    if n < 0:
        return []
    a = 0
    b = 1
    result = []
    while n > 0:
        result.append(a)
        tmp = a
        a = a + b
        b = tmp
        n = n - 1
    return result
