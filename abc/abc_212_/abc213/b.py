n = int(input())
a = list(map(int, input().split()))

print(a.index(sorted(a)[-2]) + 1)
