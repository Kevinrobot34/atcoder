def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    ans = 1
    for i in range(1, k + 1):
        ans *= n - i + 1
        ans //= i
    return ans


def perm(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    ans = 1
    for i in range(n - k + 1, n + 1):
        ans *= i
    return ans


def fact(m):
    if m < 0:
        return 0
    ans = 1
    for i in range(1, m + 1):
        ans *= i
    return ans


n = int(input())
c = [int(input()) for _ in range(n)]

div = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if c[i] % c[j] == 0:
            div[i] += 1
# print(div)

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(0, j + 1, 2):
            cnt = comb(j, k) * perm(div[i], k) * perm(n - 1 - div[i], j - k)
            # * (n-j-1)! / n!
            # print(f'i={i}(c[i]={c[i]}), j={j}, k={k}, cnt={cnt*fact(n-j-1)}')
            for l in range(n - j, n + 1):
                cnt /= l
            ans += cnt

print(ans)
