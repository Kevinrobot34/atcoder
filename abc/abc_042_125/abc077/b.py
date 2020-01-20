n = int(input())

for i in range(1, n+1):
    if (i+1)**2 > n:
        print(i**2)
        break
