n = int(input())
h = list(map(int, input().split())) + [10**10]

ans = 0
cand = 0
x = h[0]
for i in range(1, n+1):
    if x >= h[i]:
        cand += 1
    else:
        ans = max(ans, cand)
        cand = 0
    # print(i, cand)

    x = h[i]

print(ans)
