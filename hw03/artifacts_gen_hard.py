import numpy as np
from my_matrix import MyMatrix

if __name__ == '__main__':
    # ищем коллизию для матриц 2х2
    for seed in range(10000):
        np.random.seed(seed)
        data1 = np.random.randint(0, 1000, size=(2, 2))
        data2 = np.random.randint(0, 1000, size=(2, 2))
        A = MyMatrix(data1.tolist())
        C = MyMatrix(data2.tolist())
        if A.__hash__() == C.__hash__() and A._data != C._data:
            print('got \'em')

            data_eye = np.eye(2, 2)
            # почему бы и нет
            B = MyMatrix(list(data_eye))
            D = MyMatrix(list(data_eye))

            folder = 'artifacts/hard/'
            for X, s in ((A, 'A'), (B, 'B'), (C, 'C'), (D, 'D')):
                with open(folder + f'{s}.txt', 'w') as f:
                    f.write(str(X))

            AB = A @ B
            with open(folder + 'AB.txt', 'w') as f:
                f.write(str(AB))

            # кэшировано
            CD = C @ D
            with open(folder + 'CD.txt', 'w') as f:
                f.write(str(CD))

            with open(folder + 'hash.txt', 'w') as f:
                f.write(f'{str(AB.__hash__())} {(CD.__hash__())}')

            break
