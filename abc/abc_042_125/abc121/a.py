h, w = map(int, input().split())
n, m = map(int, input().split())


print(h*w - (n*w + m*h - n*m))
