n = int(input())
a = list(map(int, input().split()))

ans = 'YES' if n == len(set(a)) else 'NO'
print(ans)
