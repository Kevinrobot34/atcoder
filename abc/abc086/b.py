import math
a, b = map(int, input().split())

c = int(str(a) + str(b))
if math.sqrt(c) == int(math.sqrt(c)):
    print("Yes")
else:
    print("No")
