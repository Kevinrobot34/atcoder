n, a, b, c = map(int, input().split())
s = [input() for _ in range(n)]

is_possible = True
choice = []
ab = a + b
ac = a + c
bc = b + c

for i in range(n):
    if s[i] == 'AB':
        if ab == 0:
            is_possible = False
            break
        else:
            if ac > bc:
                choice.append('B')
                ac -= 1
                bc += 1
            elif ac == bc == 1 and i + 1 < n:
                if s[i + 1] == 'AC':
                    choice.append('A')
                    ac += 1
                    bc -= 1
                elif s[i + 1] == 'BC':
                    choice.append('B')
                    ac -= 1
                    bc += 1
                else:
                    choice.append('B')
                    ac -= 1
                    bc += 1
            else:
                choice.append('A')
                ac += 1
                bc -= 1
    elif s[i] == 'AC':
        if ac == 0:
            is_possible = False
            break
        else:
            if ab > bc:
                choice.append('C')
                ab -= 1
                bc += 1
            elif ab == bc == 1 and i + 1 < n:
                if s[i + 1] == 'AB':
                    choice.append('A')
                    ab += 1
                    bc -= 1
                elif s[i + 1] == 'BC':
                    choice.append('C')
                    ab -= 1
                    bc += 1
                else:
                    choice.append('C')
                    ab -= 1
                    bc += 1
            else:
                choice.append('A')
                ab += 1
                bc -= 1
    else:
        # BC
        if bc == 0:
            is_possible = False
            break
        else:
            if ab > ac:
                choice.append('C')
                ab -= 1
                ac += 1
            elif ab == ac == 1 and i + 1 < n:
                if s[i + 1] == 'AB':
                    choice.append('B')
                    ab += 1
                    ac -= 1
                elif s[i + 1] == 'AC':
                    choice.append('C')
                    ab -= 1
                    ac += 1
                else:
                    choice.append('C')
                    ab -= 1
                    ac += 1
            else:
                choice.append('B')
                ab += 1
                ac -= 1

if is_possible:
    print('Yes')
    print(*choice, sep='\n')
    # print('  ', 0, a, b, c)
    # for i in range(n):
    #     if s[i] == 'AB':
    #         if choice[i] == 'A':
    #             a += 1
    #             b -= 1
    #         else:
    #             a -= 1
    #             b += 1
    #     elif s[i] == 'AC':
    #         if choice[i] == 'A':
    #             a += 1
    #             c -= 1
    #         else:
    #             a -= 1
    #             c += 1
    #     else:
    #         # BC
    #         if choice[i] == 'B':
    #             b += 1
    #             c -= 1
    #         else:
    #             b -= 1
    #             c += 1
    #     print(s[i], choice[i], a, b, c)
else:
    print('No')
