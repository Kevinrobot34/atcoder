s = input()

idx = s.find("WBWBWBW")

if idx == 5:
    ans = 'Do'
elif idx == 3:
    ans = 'Re'
elif idx == 1:
    ans = 'Mi'
elif idx == 0:
    ans = 'Fa'
elif idx == 10:
    ans = 'So'
elif idx == 8:
    ans = 'La'
elif idx == 6:
    ans = 'Si'

print(ans)
