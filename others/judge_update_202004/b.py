n = int(input())
ball_r = []
ball_b = []
for _ in range(n):
    x, c = input().split()
    x = int(x)
    if c == 'R':
        ball_r.append(x)
    else:
        ball_b.append(x)

ball_r.sort()
ball_b.sort()
ans = ball_r + ball_b
print(*ans, sep='\n')
