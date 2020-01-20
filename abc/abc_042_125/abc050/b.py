n = int(input())
t = list(map(int, input().split()))
t_sum = sum(t)
m = int(input())

for i in range(m):
    p, x = map(int, input().split())
    p -= 1
    print(t_sum - t[p] + x)
