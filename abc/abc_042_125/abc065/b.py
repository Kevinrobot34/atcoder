n = int(input())
a = [int(input()) - 1 for _ in range(n)]

ans = 0
c = 0
while c != 1 and c != -1:
    c_old = c
    c = a[c]
    a[c_old] = -1
    ans += 1


if c == -1:
    ans = -1

print(ans)
