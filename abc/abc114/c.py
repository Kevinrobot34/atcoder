N = input()

ans = 0
def dfs(m):
    global ans
    if len(set(m)) == 3 and int(m) <= int(N):
        #print(m, ans)
        ans += 1

    if len(m) < len(N):
        for c in "357":
            dfs(m+c)

dfs("")
print(ans)
