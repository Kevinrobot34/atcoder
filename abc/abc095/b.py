n, x = (int(_) for _ in input().split())
m = [int(input()) for i in range(n)]

count = n
x -= sum(m)
count += int(x / min(m))
print(count)
