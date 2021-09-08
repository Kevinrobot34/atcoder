def get_divisor(n: int) -> list:
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor.append(i)
            if n // i != i:
                divisor.append(n // i)
    # divisor.sort() # if you want sorted divisors
    return divisor


x = int(input())
cand = get_divisor(x)
# print(cand)
for d in cand:
    if d**5 == x:
        print(d, 0)
    elif d**5 < x:
        a = d
        b = 0
        while a**5 - b**5 < x:
            a += 1
            b += 1
        if a**5 - b**5 == x:
            print(a, b)
            break

        a = 0
        b = -d
        while a**5 - b**5 < x:
            a -= 1
            b -= 1
        if a**5 - b**5 == x:
            print(a, b)
            break
    else:
        if d % 2 == 0 and (d // 2)**5 + (d // 2)**5 > x:
            continue
        if d % 2 == 1 and ((d + 1) // 2)**5 + (d // 2)**5 > x:
            continue
        a = d
        b = 0
        while a**5 - b**5 > x:
            a -= 1
            b -= 1
            # print(a, b, a**5 - b**5)
        if a**5 - b**5 == x:
            print(a, b)
            break

        a = 0
        b = -d
        while a**5 - b**5 > x:
            a += 1
            b += 1
        if a**5 - b**5 == x:
            print(a, b)
            break
