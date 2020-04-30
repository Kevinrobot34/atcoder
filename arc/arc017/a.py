def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True


n = int(input())
ans = 'YES' if is_prime(n) else 'NO'
print(ans)
