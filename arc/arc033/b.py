na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = len(a & b) / len(a | b)
print(ans)
