import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))

graph = [[] for i in range(n)]
for i, pi in enumerate(p):
    graph[pi].append(i + 1)

n_st = [0] * n
s_st = [0] * n


def func1(v):
    n_st[v] += 1
    for v_to in graph[v]:
        func1(v_to)
        n_st[v] += n_st[v_to]


func1(0)
# print(n_st)


def func2(v):
    if n_st[v] == 1:
        s_st[v] = 1
        return

    s_st[v] += 1
    cand1 = []
    cand2 = []
    for v_to in graph[v]:
        func2(v_to)
        if n_st[v_to] % 2 == 0:
            # s_st[v] += s_st[v_to]
            # cand1.append((n_st[v_to] - s_st[v_to], s_st[v_to]))
            cand1.append((s_st[v_to], n_st[v_to] - s_st[v_to]))
        else:
            cand2.append((s_st[v_to], n_st[v_to] - s_st[v_to]))

    cand1.sort()
    cand2.sort()

    s_st[v] += sum(x if i % 2 == 0 else y for i, (x, y) in enumerate(cand2))
    s_st[v] += sum(x if i % 2 == 0 else y for i, (x, y) in enumerate(cand1))


func2(0)
# print(s_st)

print(s_st[0])
