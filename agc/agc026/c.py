from collections import defaultdict
n = int(input())
s = input()

ans = 0

cand = defaultdict(int)
for bit in range(1 << n):
    red = []
    blue = []
    for i in range(n):
        if (bit >> i) & 1:
            red.append(s[i])
        else:
            blue.append(s[i])
    red = ''.join(red[::-1])
    blue = ''.join(blue[::-1])
    cand[(red, blue)] += 1

for bit in range(1 << n):
    red = []
    blue = []
    for i in range(n):
        if (bit >> i) & 1:
            red.append(s[n + i])
        else:
            blue.append(s[n + i])

    red = ''.join(red)
    blue = ''.join(blue)
    ans += cand[(red, blue)]

print(ans)
