import numpy as np
from mixin_matrix import MyMixinMatrix

if __name__ == '__main__':
    np.random.seed(0)
    data1 = np.random.randint(0, 10, (10, 10))
    data2 = np.random.randint(0, 10, (10, 10))
    my1 = MyMixinMatrix(data1)
    my2 = MyMixinMatrix(data2)

    res_sum = (my1 + my2)._data.tolist()
    assert res_sum == (data1 + data2).tolist()
    with open('artifacts/medium/matrix+.txt', 'w') as f:
        f.write(str(res_sum))

    res_mul = (my1 * my2)._data.tolist()
    assert res_mul == (data1 * data2).tolist()
    # asterisk in filename is not allowed (on Windows, and for a good reason)
    with open('artifacts/medium/matrix_mul.txt', 'w') as f:
        f.write(str(res_mul))

    res_matmul = (my1 @ my2)._data.tolist()
    assert res_matmul == (data1 @ data2).tolist()
    with open('artifacts/medium/matrix@.txt', 'w') as f:
        f.write(str(res_matmul))
