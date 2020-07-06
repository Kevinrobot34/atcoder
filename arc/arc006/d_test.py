h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

# for i in range(h):
#     c[i] *= 1000 // w
#
# c *= 1000 // h
#
# print(len(c), len(c[0]))
# for ci in c:
#     print(ci)

sh = 1000 // h
sw = 1000 // w
h2, w2 = h * sh, w * sw
c2 = [['.'] * w2 for _ in range(h2)]
for i in range(h2):
    for j in range(w2):
        c2[i][j] = c[i // sh][j // sw]

for i in range(h2):
    c2[i] = ''.join(c2[i])

print(h2, w2)
print(*c2, sep='\n')
