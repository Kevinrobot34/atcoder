s = {}
s['a'] = input()
s['b'] = input()
s['c'] = input()

turn = 'a'
while len(s[turn]) > 0:
    turn_next = s[turn][0]
    s[turn] = s[turn][1:]
    turn = turn_next

ans = turn.upper()

print(ans)
