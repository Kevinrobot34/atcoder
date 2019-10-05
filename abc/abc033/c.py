s = input()

sum_list = [int(s[0])]
for i in range(2, len(s), 2):
    if s[i-1] == '+':
        sum_list.append(int(s[i]))
    else:
        # s[i-1] == '*'
        sum_list[-1] *= int(s[i])

ans = len(list(filter(lambda x: x != 0, sum_list)))

print(ans)
