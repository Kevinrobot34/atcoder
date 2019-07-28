a, b = map(int, input().split())

def check(x):
    y = str(x)
    return y == y[::-1]

ans = 0
for i in range(a, b+1):
    if check(i):
        ans += 1

print(ans)
