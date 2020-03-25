n = int(input())
a = tuple(map(int, input().split()))
cnt = len(list(filter(lambda x: x % 2 == 1 or (x % 3 == 0 or x % 5 == 0), a)))
ans = 'APPROVED' if cnt == n else 'DENIED'
print(ans)
