n, a, b = map(int, input().split())

def sum_all_digits(m):
    res = 0
    while m > 0:
        res += m % 10
        m = m // 10
    return res

ans = 0
for i in range(1, n+1):
    s = sum_all_digits(i)
    if a <= s and s <= b:
        ans += i

print(ans)
