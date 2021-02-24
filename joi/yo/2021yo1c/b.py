n = int(input())
s = input()

ans = 0
for i in range(n):
    if i % 2 == 0 and s[i] != 'I':
        ans += 1
    elif i % 2 == 1 and s[i] != 'O':
        ans += 1

print(ans)
