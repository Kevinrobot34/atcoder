n = 6
e = set(map(int, input().split()))
b = int(input())
l = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if l[i] in e:
        cnt += 1

if cnt == 6:
    ans = '1'
elif cnt == 5:
    for i in range(n):
        if l[i] not in e:
            ans = '2' if l[i] == b else '3'
            break
elif cnt == 4:
    ans = '4'
elif cnt == 3:
    ans = '5'
else:
    ans = '0'

print(ans)
