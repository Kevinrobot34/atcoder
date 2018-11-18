a,b,c,x,y = (int(_) for _ in input().split())

cost = min(x,y) * min(a+b, 2*c)
if x>y:
    cost += (x-y)*min(a, 2*c)
else:
    cost += (y-x)*min(b, 2*c)

print(cost)
