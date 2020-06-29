a, b = map(int, input().split())

if abs(a) < abs(b):
    ans = 'Ant'
elif abs(a) == abs(b):
    ans = 'Draw'
else:
    ans = 'Bug'

print(ans)
