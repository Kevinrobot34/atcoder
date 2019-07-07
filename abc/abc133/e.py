import sys
sys.setrecursionlimit(10**7 + 10)

MOD = 10**9 + 7

n, k = map(int, input().split())
e = [[] for i  in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

if n == 1:
    print(k)
else:
    visited = [False for i in range(n)]
    def dfs(v, npv, nppv):
        global visited
        ans = max(k - npv - nppv, 0)
        visited[v] = True
        i = 0
        for nv in e[v]:
            if visited[nv]:
                continue

            ans *= dfs(nv, 1, npv+i)
            ans = ans % MOD
            i += 1

        return ans

    for i in range(n):
        if len(e[i]) == 1:
            # print(i)
            s = i
            break

    print(dfs(s, 0, 0))

    # print(e)
