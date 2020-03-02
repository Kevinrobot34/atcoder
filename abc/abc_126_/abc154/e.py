from itertools import combinations


def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1

    ans = n
    for i in range(2, k + 1):
        ans *= (n + 1 - i)
        ans //= i
    return ans


n_str = input()  # 3***
k = int(input())

ans = 0

# 3***
if k == 2:
    ans += int(n_str)
elif k == 3:
    pass

# 1***
ans += int(n_str[0] - 1) * comb(len(n_str) - 1, k - 1) * (9**(k - 1))
# 0***
ans += comb(len(n_str) - 1, k) * (9**k)
