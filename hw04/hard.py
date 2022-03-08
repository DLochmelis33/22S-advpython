from multiprocessing import Process, Queue, Pipe
from datetime import datetime
import time
import codecs


def print_msg(msg):
    print(f'{datetime.now().time()}: {msg}')


def main_routine(queue):
    while(True):
        msg = str(input("enter message: "))
        queue.put(msg)


def a_routine(queue, conn1):
    while(True):
        msg = queue.get()
        time.sleep(5)  # simulate proccessing
        conn1.send(msg.lower())


def b_routine(conn2):
    while(True):
        msg = conn2.recv()
        encoded = codecs.encode(msg, 'rot_13')
        print_msg(encoded)


if __name__ == '__main__':
    queue = Queue()
    conn1, conn2 = Pipe()
    a_process = Process(target=a_routine, args=(queue, conn1))
    b_process = Process(target=b_routine, args=(conn2,))

    b_process.start()
    a_process.start()
    main_routine(queue)
