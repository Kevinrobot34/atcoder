n = int(input())

ans = n
for a in range(1, n):
    if a * a > n:
        break
    if n % a != 0:
        continue

    b = n // a
    ans = min(ans, max(len(str(a)), len(str(b))))

print(ans)
