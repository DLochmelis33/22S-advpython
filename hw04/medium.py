import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import numpy as np
import multiprocessing
import time


def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


class Job:  # trick to make a picklable lambda (for multiprocessing)

    def __init__(self, a, f, step, enable_logs=False):
        self.a = a
        self.f = f
        self.step = step
        self.enable_logs = enable_logs

    def __call__(self, inds):
        if self.enable_logs:
            print(f'task with id {inds[0]} started')
        part_sum = 0
        a = self.a
        f = self.f
        step = self.step
        for i in inds:
            part_sum += f(a + i * step) * step
        return part_sum


def integrate_multithread(f, a, b, *, is_proc, n_jobs=1, n_iter=1000, enable_logs=False):
    def pool_ctor(threads):
        return ProcessPoolExecutor(threads) if is_proc else ThreadPoolExecutor(threads)
    with pool_ctor(n_jobs) as executor:
        acc = 0
        step = (b - a) / n_iter
        return sum(executor.map(Job(a, f, step, enable_logs), np.array_split(range(n_iter), n_jobs)))


if __name__ == "__main__":
    cpu_num = multiprocessing.cpu_count()
    n_iter = int(3e6)

    for n_jobs in range(1, cpu_num * 2 + 1):
        start = time.time()
        integrate_multithread(math.cos, 0, math.pi / 2,
                              is_proc=True, n_jobs=n_jobs, n_iter=n_iter)
        # integrate(math.cos, 0, math.pi / 2, n_iter=n_iter)
        end = time.time()
        total_time = end - start
        print(f'{total_time}')
