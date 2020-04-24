n, m, d = map(int, input().split())
a = tuple(map(int, input().split()))
amida = list(range(n))
for ai in reversed(a):
    amida[ai - 1], amida[ai] = amida[ai], amida[ai - 1]

ans = [-1] * n
for i in range(n):
    if ans[i] != -1:
        continue
    cycle = [i]
    while i != amida[cycle[-1]]:
        cycle.append(amida[cycle[-1]])

    s = len(cycle)
    for j in range(s):
        ans[cycle[j]] = cycle[(j + d) % s] + 1

# print(amida)
print(*ans, sep='\n')
