from collections import defaultdict


def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans


n, p = map(int, input().split())
s = input()

if p == 2:
    ans = 0
    for i in range(n):
        if int(s[i]) % 2 == 0:
            ans += i + 1
elif p == 5:
    ans = 0
    for i in range(n):
        if int(s[i]) in [0, 5]:
            ans += i + 1
else:
    mod_list = [0] * (n + 1)
    d = 1
    for i in reversed(range(n)):
        mod_list[i] = int(s[i]) * d + mod_list[i + 1]
        mod_list[i] %= p
        d = (d * 10) % p

    mod_dict = defaultdict(int)
    for i in range(n + 1):
        mod_dict[mod_list[i]] += 1

    # print(mod_list)
    # print(mod_dict)

    ans = 0
    for c in mod_dict:
        ans += comb(mod_dict[c], 2)

print(ans)
