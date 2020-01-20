s = input()

si = 0
while s[si] != 'A':
    si += 1

ei = len(s) - 1
while s[ei] != 'Z':
    ei -= 1

ans = ei - si + 1

print(ans)
