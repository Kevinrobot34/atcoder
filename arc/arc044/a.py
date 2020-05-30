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
if n == 1:
    ans = 'Not Prime'
elif is_prime(n):
    ans = 'Prime'
elif n % 2 != 0 and n % 5 != 0 and n % 3 != 0:
    ans = 'Prime'
else:
    ans = 'Not Prime'
print(ans)
