def func(b, n):
    res = 0
    while n > 0:
        res += n % b
        n //= b
    return res


def solve():
    n = int(input())
    s = int(input())

    if n == s:
        return n + 1
    elif n < s:
        return -1

    for b in range(2, n + 1):
        if b**2 > n:
            break
        if func(b, n) == s:
            return b

    b_cand = []
    for p in range(1, n + 1):
        if p**2 > n:
            break
        b = (n - s) // p + 1
        if b > 1:
            b_cand.append(b)
    b_cand = b_cand[::-1]

    for b in b_cand:
        # print(b)
        if func(b, n) == s:
            return b

    return -1


ans = solve()
print(ans)
