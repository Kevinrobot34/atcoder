s = input()

if s[0] == s[-1]:
    # 最終的には 'ababa' 的な感じの長さ奇数の文字列になる
    if len(s) % 2 == 0:
        ans = 'First'
    else:
        ans = 'Second'
else:
    # 最終的には 'ababab' 的な感じの長さ偶数の文字列になる
    if len(s) % 2 == 0:
        ans = 'Second'
    else:
        ans = 'First'

print(ans)
