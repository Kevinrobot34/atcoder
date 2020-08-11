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
divisor = get_divisor(n)
ans = 0
for x in divisor:
    if n == x:
        continue
    m = n // x - 1
    if n // m == n % m:
        ans += m

print(ans)
