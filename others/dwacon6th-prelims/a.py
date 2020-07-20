n = int(input())
songs = []
for _ in range(n):
    s, t = input().split()
    t = int(t)
    songs.append((s, t))
x = input()

ans = 0
flag = False
for s, t in songs:
    if flag:
        ans += t
    if s == x:
        flag = True

print(ans)
