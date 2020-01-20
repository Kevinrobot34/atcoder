x = int(input())

ans = 1
for b in range(2, x+1):
    if b ** 2 > x:
        continue

    p = 2
    while b ** (p+1) <= x:
        p += 1
    ans = max(ans, b ** p)

print(ans) 
