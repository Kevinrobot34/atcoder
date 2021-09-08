def main():
    import numpy as np
    from operator import itemgetter
    import sys

    input = sys.stdin.readline

    n = int(input())
    koma = [np.array((*map(int, input().split()), 1)) for _ in range(n)]
    m = int(input())
    ops = [input() for _ in range(m)]
    q = int(input())
    queries = [(*map(int, input().split()), i) for i in range(q)]
    queries.sort(key=itemgetter(0))

    ans = [None] * q
    matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    mat0 = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    mat1 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

    def get_matrix(ops_str):
        i = int(ops_str[0]) - 1
        if i == 0:
            return mat0
        elif i == 1:
            return mat1
        else:
            p = int(ops_str[2:])
            if i == 2:
                return np.array([[-1, 0, 2 * p], [0, 1, 0], [0, 0, 1]])
            else:
                return np.array([[1, 0, 0], [0, -1, 2 * p], [0, 0, 1]])

    m_curr = 0
    for ai, bi, i in queries:
        bi -= 1
        while m_curr < ai:
            a = get_matrix(ops[m_curr])
            matrix = np.dot(a, matrix)
            m_curr += 1
        x = np.dot(matrix, koma[bi])
        ans[i] = f'{x[0]} {x[1]}'

    print(*ans, sep='\n')


main()
