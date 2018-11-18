s = input()

dp1 = {'A': 0, 'AB': 0, 'ABC': 0}
dp2 = {'A': 0, 'AB': 0, 'ABC': 0}

c = 1000000000 + 7
n = len(s)
tmp = [1]*n
for i in range(1, n):
    tmp[i] = (tmp[i-1] * 3)%c

count = 0
for i in range(n):
    if s[i] == '?':
        dp2['A'] = dp1['A']*3 + tmp[count]
        dp2['AB'] = dp1['AB']*3 + dp1['A']
        dp2['ABC'] = dp1['ABC']*3 + dp1['AB']
        count += 1
    elif s[i] == 'A':
        dp2['A'] = dp1['A'] + tmp[count]
        dp2['AB'] = dp1['AB']
        dp2['ABC'] = dp1['ABC']
    elif s[i] == 'B':
        dp2['A'] = dp1['A']
        dp2['AB'] = dp1['AB'] + dp1['A']
        dp2['ABC'] = dp1['ABC']
    elif s[i] == 'C':
        dp2['A'] = dp1['A']
        dp2['AB'] = dp1['AB']
        dp2['ABC'] = dp1['ABC'] + dp1['AB']

    dp1['ABC'] = dp2['ABC'] % c
    dp1['AB'] = dp2['AB'] % c
    dp1['A'] = dp2['A'] % c

    #print(i, dp1)

print(dp1['ABC'])
