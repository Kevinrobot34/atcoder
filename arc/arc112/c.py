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


def func2(v):
    if n_st[v] == 1:
        s_st[v] = 1
        return

    s_st[v] += 1
    bonus = 0
    cand = []
    for v_to in graph[v]:
        func2(v_to)
        if n_st[v_to] % 2 == 0:
            if s_st[v_to] < 0:
                s_st[v] += s_st[v_to]
            else:
                bonus += s_st[v_to]
        else:
            cand.append(s_st[v_to])

    cand.sort()
    s_st[v] += sum(cand[0::2])
    s_st[v] -= sum(cand[1::2])
    if len(cand) % 2 == 0:
        s_st[v] += bonus
    else:
        s_st[v] -= bonus


func1(0)  # calc num of sub tree verticies
# print(n_st)
func2(0)  # calc diff-score of sub tree
# print(s_st)
ans = (n + s_st[0]) // 2
print(ans)
