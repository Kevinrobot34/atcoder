import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = True
    graph[b][a] = True


def check_comp(bit):
    targets = [i for i in range(n) if (bit >> i) & 1]
    for i in range(len(targets)):
        for j in range(i):
            if not graph[targets[i]][targets[j]]:
                return False
    return True


is_comp = [check_comp(bit) for bit in range(1 << n)]
is_comp[0] = False
memo = {}
ans = 0


def func(sup):
    if sup == 0:
        return 0
    if is_comp[sup]:
        return 1
    if sup in memo:
        return memo[sup]

    ret = n
    sub = (sup - 1) & sup
    while True:
        if is_comp[sub]:
            # print(sup, bin(sup), bin(sub), bin(sub ^ sup))
            r1 = func(sub)
            if r1 + 1 < ret:
                ret = min(ret, r1 + func(sup ^ sub))
            # print(bin(sup), bin(sub))
        sub = (sub - 1) & sup
        if sub == 0:
            break

    memo[sup] = ret
    return ret


ans = func((1 << n) - 1)
print(ans)
