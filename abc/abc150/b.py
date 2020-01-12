n = int(input())
s = input()

ans = 0
i = 0
while i < n - 2:
    if s[i:i + 3] == 'ABC':
        ans += 1
        i += 3
    else:
        i += 1

print(ans)
