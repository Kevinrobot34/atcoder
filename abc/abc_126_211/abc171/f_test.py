k = int(input())
s = input()
n = len(s)

x = set()
for i in range(n + 1):
    for j in range(26):
        x.add(s[:i] + chr(ord('a') + j) + s[i:])

x = sorted(list(x))
print(x)
print(len(x))
