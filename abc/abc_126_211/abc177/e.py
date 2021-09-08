from collections import Counter


def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


def check_pairwise_coprime(a):
    m = max(a)
    cnt_a = Counter(a)
    is_prime = [True] * (m + 1)
    for i in range(2, m // 2 + 1):
        if is_prime[i]:
            cnt = cnt_a[i]
            for j in range(2, m // i + 1):
                cnt += cnt_a[i * j]
                is_prime[i * j] = False
            if cnt > 1:
                return False
    return True


def check_setwise_coprime(a):
    gcd_all = a[0]
    for i in range(1, n):
        gcd_all = GCD(gcd_all, a[i])
    return gcd_all == 1


n = int(input())
a = list(map(int, input().split()))

if check_pairwise_coprime(a):
    print('pairwise coprime')
elif check_setwise_coprime(a):
    print('setwise coprime')
else:
    print('not coprime')
