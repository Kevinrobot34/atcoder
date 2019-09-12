s = input()

def dfs(s):
    ans = int(s)
    for i in range(1, len(s)):
        ans += int(s[:i]) * (1 << (len(s[i:])-1)) + dfs(s[i:])
    return ans

ans = dfs(s)
print(ans)
