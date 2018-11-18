d, g = (int(_) for _ in input().split())
p = [0]*d
c = [0]*d
for i in range(d):
    p[i], c[i] = (int(_) for _ in input().split())

q = [(p[i], 100*(i+1)*p[i]+c[i], 100*(i+1)+float(c[i]/p[i]), i) for i in range(d)]

q = sorted(q, key=lambda x:(-x[1], x[0]))
#print(q[0], q[0][1], q[0][-1])

count = 0
while g > 0 :
    if g >= q[0][1]:
        q = sorted(q, key=lambda x:(-x[2], -x[1]))
        g -= q[0][1]
        count += q[0][0]
        q.pop(0)
        q = sorted(q, key=lambda x:(-x[1], x[0]))
    else:
        q = sorted(q, key=lambda x:(x[0], -x[1]))
        idx = 0
        while g > q[idx][1]:
            idx += 1
        tmp1 = q[idx][0]
        #print('g', g)
        #print('tmp1', tmp1)

        idx = max([x for _,_,_,x in q])
        #print(idx, p[idx])
        if int(g/(100*(idx+1)) + 0.5) <= p[idx]:
            tmp2 = int(g/(100*(idx+1)) + 0.5)
            #print('tmp2', tmp2)

            count += min(tmp1, tmp2)
        else:
            count += tmp1
        g=0

    #print(count)

print(count)
