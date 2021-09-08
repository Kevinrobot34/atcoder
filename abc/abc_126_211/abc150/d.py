def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)


n, m = map(int, input().split())
a = list(map(lambda x: int(x) // 2, input().split()))

a_lcm = a[0]
for i in range(1, n):
    a_lcm = LCM(a_lcm, a[i])
    if a_lcm > m:
        break

if a_lcm <= m:
    flag = True
    for i in range(n):
        if (a_lcm // a[i]) % 2 == 0:
            flag = False
            break

    if flag:
        ans = ((m // a_lcm) + 1) // 2
    else:
        ans = 0
else:
    ans = 0
print(ans)
