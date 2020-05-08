n = int(input())
a = list(map(int, input().split()))
ans = 0
cand = [9, 7, 3, 1]
for ai in a:
    for cj in cand:
        if cj <= ai:
            ans += ai - cj
            break

print(ans)
