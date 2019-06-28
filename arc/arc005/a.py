n = int(input())
words = [w for w in input().rstrip('.').split()]

chokudai = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
ans = 0
for w in words:
    if w in chokudai:
        ans += 1

print(ans)
