s = input()
cnt = s.count('o')
ans = 'YES' if cnt + (15 - len(s)) >= 8 else 'NO'
print(ans)
