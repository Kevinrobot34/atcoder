n = int(input())
a = list(map(int, input().split()))

d = [1.0 / ai for ai in a]
print(1.0 / sum(d))
