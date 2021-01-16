n, k = map(int, input().split())
s = input()

d = {
    ('R', 'R'): 'R',
    ('R', 'P'): 'P',
    ('R', 'S'): 'R',
    ('P', 'R'): 'P',
    ('P', 'P'): 'P',
    ('P', 'S'): 'S',
    ('S', 'R'): 'R',
    ('S', 'P'): 'S',
    ('S', 'S'): 'S',
}
while k:
    if len(s) % 2 == 1:
        s *= 2
    s = ''.join(d[(s[i], s[i + 1])] for i in range(0, len(s), 2))
    k -= 1

print(s[0])
