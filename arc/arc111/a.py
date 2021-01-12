n, m = map(int, input().split())

q, r = (10 // m) % m, 10 % m
aq, ar = 0, 1
x = 1
while n > 0:
    if n % 2 == 1:
        aq, ar = (aq * r + ar * q + (ar * r) // m) % m, (ar * r) % m
    q, r = (2 * q * r + (r**2) // m) % m, (r**2) % m
    n = n // 2

print(aq)
