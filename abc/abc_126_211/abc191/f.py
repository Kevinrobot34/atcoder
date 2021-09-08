import math
n = int(input())
a = list(map(int, input().split()))

gcd_list = [[math.gcd(ai, aj) for aj in a] for ai in a]
a_min = min(a)
cand = set([a_min])
for i in range(n):
    for j in range(i + 1, n):
        if gcd_list[i][j] <= a_min:
            cand.add(gcd_list[i][j])
ans = len(cand)
# print(*gcd_list, sep='\n')
print(ans)
