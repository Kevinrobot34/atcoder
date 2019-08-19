n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

def temperature(x):
    return t - x * 0.006

ans = 0
for i in range(1, n):
    if abs(a - temperature(h[ans])) > abs(a - temperature(h[i])):
        ans = i
print(ans + 1)
