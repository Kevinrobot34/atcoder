n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = [a[i], i+1]

a.sort(reverse=True)

for i in range(n):
    print(a[i][1])
