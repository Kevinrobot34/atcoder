def eratosthenes(n: int) -> list:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n // 2 + 1):
        if is_prime[i]:
            for j in range(2, n // i + 1):
                is_prime[i * j] = False
    return is_prime


x = int(input())
is_prime = eratosthenes(x * 2 + 100)
ans = x
while not is_prime[ans]:
    ans += 1
print(ans)
