N = input()

def dfs(m):
    ans = 0
    if len(set(m)) == 3 and int(m) <= int(N):
        ans += 1

    if len(m) < len(N):
        for c in ['3', '5', '7']:
            ans += dfs(m + c)

    return ans

print(dfs(""))
