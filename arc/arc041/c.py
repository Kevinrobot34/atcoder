n, l = map(int, input().split())
ans = 0
rabbits = []
for _ in range(n):
    x, d = input().split())
    x = int(x)
    if len(rabbits) == 0 and d =='L':
        ans += x-1
    else:
        rabbits.append((x, d))

while rabbits[-1][1] == 'R':
    ans += 0
