h = int(input())
w = int(input())
n = int(input())

x = max(h, w)
ans = (n + x - 1) // x
print(ans)
