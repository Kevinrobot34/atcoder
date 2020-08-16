from collections import Counter
n = int(input())
a = list(map(int, input().split()))

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

    cnt = Counter(a_cs)
    ans = sum(v * (v - 1) // 2 for v in cnt.values())
    print(ans)
