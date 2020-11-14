import numpy as np


def func(mat: np.ndarray, v: np.ndarray, n: int, MOD: int) -> int:
    while n > 0:
        if n % 2 == 1:
            v = np.dot(mat, v) % MOD
        mat = np.dot(mat, mat) % MOD
        n //= 2
    return v[0]


n_bit = 32
k, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

if k < m:
    mat_list = [
        np.roll(np.identity(k, dtype=int), -1, axis=1) for _ in range(n_bit)
    ]
    for j in range(n_bit):
        mat_list[j][0] = np.array([(ci >> j) & 1 for ci in c])

    v = np.array(a[::-1]).T
    v_list = [np.array([(vi >> j) & 1 for vi in v]).T for j in range(n_bit)]
    # print(*v_list, sep='\n')

    ans_bit = [func(mat_list[j], v_list[j], m - k, 2) for j in range(n_bit)]
    # print(ans_bit)
    ans = sum((1 << j) * bj for j, bj in enumerate(ans_bit))
    print(ans)
else:
    print(a[m - 1])
