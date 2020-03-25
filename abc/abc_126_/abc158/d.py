from collections import deque

s = input()
q = int(input())
is_reverse = False

d = deque(list(s))
for _ in range(q):
    qi = input()
    if len(qi) == 1:
        # query 1
        is_reverse = not is_reverse
    else:
        # query 2
        _, f, c = qi.split()
        f1 = f == '1'
        if f1 == is_reverse:
            d.append(c)
        else:
            d.appendleft(c)

d = list(d)
if is_reverse:
    d = d[::-1]
ans = ''.join(d)
print(ans)
