from operator import itemgetter
import sys


def multiple_mm(matrix1, matrix2):
    (a1, b1), (c1, d1) = matrix1
    (a2, b2), (c2, d2) = matrix2
    return [
        [a1 * a2 + b1 * c2, a1 * b2 + b1 * d2],
        [c1 * a2 + d1 * c2, c1 * b2 + d1 * d2],
    ]


def multiple_mv(matrix, x):
    (a, b), (c, d) = matrix
    return [a * x[0] + b * x[1], c * x[0] + d * x[1]]


def func(matrix, offset, x):
    y = multiple_mv(matrix, x)
    return [y[0] + offset[0], y[1] + offset[1]]


def main():
    input = sys.stdin.readline

    n = int(input())
    koma = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    ops = [input() for _ in range(m)]
    q = int(input())
    queries = [list(map(int, input().split())) + [i] for i in range(q)]
    queries.sort()

    ans = [None] * q
    matrix = [[1, 0], [0, 1]]
    offset = [0, 0]

    mat_list = [
        [[0, 1], [-1, 0]],
        [[0, -1], [1, 0]],
        [[-1, 0], [0, 1]],
        [[1, 0], [0, -1]],
    ]

    def get_matrix(ops_str):
        i = int(ops_str[0]) - 1
        return mat_list[i]

    def get_offset(ops_str):
        i = int(ops_str[0]) - 1
        if i <= 1:
            return [0, 0]
        elif i == 2:
            p = int(ops_str.split()[1])
            return [2 * p, 0]
        else:
            p = int(ops_str.split()[1])
            return [0, 2 * p]

    m_curr = 0
    for ai, bi, i in queries:
        bi -= 1
        while m_curr < ai:
            a = get_matrix(ops[m_curr])
            b = get_offset(ops[m_curr])
            matrix = multiple_mm(a, matrix)
            offset = func(a, b, offset)
            m_curr += 1
        x = func(matrix, offset, koma[bi])
        ans[i] = f'{x[0]} {x[1]}'

    print(*ans, sep='\n')


main()
