from multiprocessing import Process
from typing import List
import time


def fib(n: int) -> List[int]:  # copied from hw01
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


def time_fib(n, call_count, proc_count):
    total_time = 0
    for c in range(call_count):
        print(c)
        # proc_list = []
        # for p in range(proc_count):
        #     proc_list.append(Process(target=fib, args=(n,)))

        start = time.time()
        
        # for proc in proc_list:
        #     proc.start()

        # for proc in proc_list:
        #     proc.join()
        for p in range(proc_count):
            fib(n)

        end = time.time()
        total_time += end - start
    return total_time / call_count


if __name__ == '__main__':
    print(f'avg time: {time_fib(n=100000, call_count=10, proc_count=10)}')
