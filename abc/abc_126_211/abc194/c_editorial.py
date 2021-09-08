from collections import Counter

n = int(input())
a = list(map(int, input().split()))
a_cnt = Counter(a)

ans = 0
for ai, ci in a_cnt.items():
    for aj, cj in a_cnt.items():
        ans += ci * cj * (ai - aj)**2
ans //= 2
print(ans)
