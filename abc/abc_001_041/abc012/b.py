n = int(input())
s = n % 60
n = n // 60
m = n % 60
h = n // 60
print('{0:02d}:{1:02d}:{2:02d}'.format(h, m, s))
