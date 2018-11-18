s = str(input())
n = int(input())

cand = [str(s[0])]
for i in range(len(s)):
    if len(cand) == n and s[i] > cand[-1]:
        continue
    for j in range(i, len(s)):
        tmp = s[i:j+1]
        #print(i,j, tmp, cand)
        if len(cand) == n and tmp > cand[-1]:
            break
        if tmp in cand:
            continue
        cand += [tmp]
        #cand = sorted(cand)
        cand.sort()
        if len(cand) > n:
            cand.pop()


print(cand.pop())
