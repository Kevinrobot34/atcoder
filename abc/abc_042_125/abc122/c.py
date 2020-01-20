n, q = map(int, input().split())
s = input()

x = [0] * (n+1)
for i in range(1, n):
    if s[i-1] == "A" and s[i] == "C":
        x[i+1] = 1
for i in range(n):
    x[i+1] += x[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(x[r] - x[l])
