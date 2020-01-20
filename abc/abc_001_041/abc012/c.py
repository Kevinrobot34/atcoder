n = int(input())

m = 45**2 - n
for i in range(1, 10):
    if m % i == 0 and m // i < 10:
        print("{} x {}".format(i, m // i))
