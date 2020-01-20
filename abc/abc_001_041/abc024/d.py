x = int(input())
y = int(input())
z = int(input())

p = z * (x - y)
r = p / (-p - y * x)
q = y * (x - z)
c = q / (-q - z * x)

print(r, c)
