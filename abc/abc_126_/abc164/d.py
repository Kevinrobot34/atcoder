from collections import Counter


def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans


s = input()
n = len(s)
a = [0] * (n + 1)
a[n - 1] = int(s[n - 1])
base = 10
for i in reversed(range(n - 1)):
    a[i] = (a[i + 1] + int(s[i]) * base) % 2019
    base *= 10
    base %= 2019
# print(a)

cnt = Counter(a)
# print(cnt)

ans = 0
for v in cnt.values():
    ans += comb(v, 2)

print(ans)
