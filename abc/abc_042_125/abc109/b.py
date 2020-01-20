n = int(input())
w0 = input()
word_set = set([w0])
ans = True

for i in range(1, n):
    w = input()
    if ans and w not in word_set and w[0] == w0[-1]:
        word_set.add(w)
        w0 = w
    else:
        ans = False

if ans:
    print("Yes")
else:
    print("No")
