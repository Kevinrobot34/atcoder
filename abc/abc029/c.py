n = int(input())

def dfs(s):
    if len(s) == n:
        print(s)
    else:
        for c in ['a', 'b', 'c']:
            dfs(s + c)

dfs('')
