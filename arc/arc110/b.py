n = int(input())
t = input()

x = '110' * ((n + 2) // 3)
y = x + '110'

if t == '1':
    ans = 10**10 * 2
elif t in x:
    ans = 10**10 - (n + 2) // 3 + 1
elif t in y:
    ans = 10**10 - (n + 2) // 3
else:
    ans = 0

print(ans)
