t = 'indeednow'
n = int(input())
for _ in range(n):
    s = input()
    ans = 'YES' if ''.join(sorted(s)) == ''.join(sorted(t)) else 'NO'
    print(ans)
