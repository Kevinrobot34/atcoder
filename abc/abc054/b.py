n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

def check():
    for i in range(n-m+1):
        for j in range(n-m+1):
            for k in range(m):
                if b[k] != a[j+k][i:i+m]:
                    break
            else:
                return "Yes"

    return "No"

ans = check()

print(ans)
