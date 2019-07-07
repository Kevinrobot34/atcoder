def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

a, b, k = map(int, input().split())

n = 0

for i in reversed(range(1, GCD(a, b)+1)):
    if a % i == 0 and b % i == 0:
        n += 1

    if n == k:
        print(i)
        break
