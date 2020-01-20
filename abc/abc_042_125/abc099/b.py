a, b = map(int, input().split())

c = b - a - 1
print(c*(c+1)//2 - a)
