import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    graph[ai].append(bi)
    graph[bi].append(ai)
c = list(map(int, input().split()))
c.sort()

s = sum(c[:-1])
ans = [-1] * n


def func(v, v_par):
    ans[v] = c.pop()
    for v_to in graph[v]:
        if v_to == v_par:
            continue
        func(v_to, v)


func(0, -1)
print(s)
print(*ans)
