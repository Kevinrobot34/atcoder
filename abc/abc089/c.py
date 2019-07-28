n = int(input())
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0, }
t = "MARCH"
for i in range(n):
    s = input()
    if s[0] in d:
        d[s[0]] += 1

ans = 0
for bits in range(1<<5):
    bits_list = [i for i in range(5) if (bits >> i) & 1 == 1]
    if len(bits_list) == 3:
        ans += d[t[bits_list[0]]] * d[t[bits_list[1]]] * d[t[bits_list[2]]]

print(ans)
