def get_divisor(n: int) -> list:
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor.append(i)
            if n // i != i:
                divisor.append(n // i)
    return divisor


n = int(input())
ans = 0
m_cand = get_divisor(2 * n)
for m in m_cand:
    if abs(2 * n - m * (m - 1)) % (2 * m) == 0:
        ans += 1
print(ans)
