n, m = map(int, input().split())

p = m // n
while m % p != 0:
    p -= 1

print(p)
