s = input()
n = int(input())

for _ in range(n):
    l, r = map(int, input().split())
    l -= 1
    s = s[:l] + s[l:r][::-1] + s[r:]

print(s)
