from collections import defaultdict


def get_divisor(n: int) -> list:
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor.append(i)
            if n // i != i:
                divisor.append(n // i)
    # divisor.sort() # if you want sorted divisors
    return divisor


n = int(input())

d0 = get_divisor(n)
ans0 = 0  # n自身
for di in d0:
    if di == 1:
        continue
    x = n // di
    while x % di == 0:
        x = x // di
    if x % di == 1:
        # print(di)
        ans0 += 1

d1 = get_divisor(n - 1)
ans1 = len(d1) - 1

ans = ans0 + ans1
# print(n - 1, ':', d1)
# print(n, ':', d0)
print(ans)
