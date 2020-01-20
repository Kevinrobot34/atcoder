n = int(input())
a = list(map(int, input().split()))

def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)

l = [0]
r = [0]
for i in range(n):
    l.append(GCD(l[i], a[i]))
    r.append(GCD(r[i], a[n-1 - i]))
r = r[::-1]

ans = 1
for i in range(n):
    ans = max(ans, GCD(l[i], r[i+1]))

print(ans)
