n, l = map(int, input().split())
s = input()

t = 1
ans = 0
for i in range(n):
    if s[i] == '+':
        t += 1
    else:
        t -= 1

    if t > l:
        ans += 1
        t = 1

print(ans)
