from collections import defaultdict
n = int(input())
a = tuple(map(int, input().split()))


def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans


d = defaultdict(int)
comb_list = [0] * n
for ai in a:
    d[ai] += 1

ans_sum = 0
for i in d:
    ans_sum += comb(d[i], 2)

for i in range(n):
    ans_i = ans_sum - comb(d[a[i]], 2) + comb(d[a[i]] - 1, 2)
    print(ans_i)
