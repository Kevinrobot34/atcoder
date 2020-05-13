c = [input() for _ in range(4)]
for i in reversed(range(4)):
    print(''.join(c[i][::-1]))
