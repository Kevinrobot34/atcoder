import sys
sys.setrecursionlimit(10**8)

s = input()

words = ['dream', 'dreamer', 'erase', 'eraser']
def dfs(idx):
    if idx == len(s):
        return True
    ans = False
    for word in words:
        if s[idx:idx+len(word)] == word:
            ans = ans or dfs(idx + len(word))

    return ans

if dfs(0):
    print("YES")
else:
    print("NO")
