n = int(input())
a = list(map(int, input().split()))

s = 0
for ai in a:
    s = s ^ ai

ans = [s ^ ai for ai in a]
print(*ans)
