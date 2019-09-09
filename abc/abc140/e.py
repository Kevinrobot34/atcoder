n = int(input())
p = map(int, input().split())

ans = 0
for i in range(n-1):
    pm1 = p[i]
    pm2 = p[i+1]
    for j in range(i+1, n):
        
