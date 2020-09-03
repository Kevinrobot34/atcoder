from copy import deepcopy
import sys
input = sys.stdin.readline


def warshall_floyd(d):
    # d        : nxn adjacent matrix
    # next_node: node after i on the shortest path of (i,j)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


def check(a, b):
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if b[i][j] < a[i][j]:
                return -1
            flag = True
            for k in range(n):
                if k == i or k == j:
                    continue
                if b[i][j] == b[i][k] + b[k][j]:
                    flag = False
                    break
            if flag:
                res += a[i][j]
    return res


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = deepcopy(a)
warshall_floyd(b)
ans = check(a, b)
print(ans)
