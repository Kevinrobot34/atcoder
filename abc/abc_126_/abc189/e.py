import numpy as np
from operator import itemgetter
import sys


def main():
    input = sys.stdin.readline

    n = int(input())
    koma = [np.array(list(map(int, input().split()))).T for _ in range(n)]
    m = int(input())
    ops = [input() for _ in range(m)]
    q = int(input())
    queries = [list(map(int, input().split())) + [i] for i in range(q)]
    queries.sort()

    ans = [None] * q
    matrix = np.array([[1, 0], [0, 1]])
    offset = np.array([0, 0]).T

    mat_list = [
        np.array([[0, 1], [-1, 0]]),
        np.array([[0, -1], [1, 0]]),
        np.array([[-1, 0], [0, 1]]),
        np.array([[1, 0], [0, -1]]),
    ]

    def get_matrix(ops_str):
        i = int(ops_str[0]) - 1
        return mat_list[i]

    def get_offset(ops_str):
        i = int(ops_str[0]) - 1
        if i <= 1:
            return np.array([0, 0]).T
        elif i == 2:
            p = int(ops_str.split()[1])
            return np.array([2 * p, 0]).T
        else:
            p = int(ops_str.split()[1])
            return np.array([0, 2 * p]).T

    m_curr = 0
    for ai, bi, i in queries:
        bi -= 1
        while m_curr < ai:
            a = get_matrix(ops[m_curr])
            b = get_offset(ops[m_curr])
            matrix = np.dot(a, matrix)
            offset = np.dot(a, offset) + b
            m_curr += 1
        x = np.dot(matrix, koma[bi]) + offset
        ans[i] = f'{x[0]} {x[1]}'

    print(*ans, sep='\n')


main()
