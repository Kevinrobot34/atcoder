n = int(input())
b = [int(input()) for _ in range(n)]
a = [0]

for i in range(n - 1):
    a.append(a[-1] ^ b[i])

if a[0] ^ a[-1] == b[-1]:
    print(*a, sep='\n')
else:
    print(-1)
