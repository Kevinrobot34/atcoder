def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n):
    ans = GCD(ans, a[i])

print(ans)
