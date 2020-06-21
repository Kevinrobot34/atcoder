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
m = sum(get_divisor(n)) - n
if m < n:
    ans = 'Deficient'
elif m == n:
    ans = 'Perfect'
else:
    ans = 'Abundant'
print(ans)
