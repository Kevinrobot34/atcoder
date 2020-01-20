a = input()
b = input()

max_len = 105

if len(a) < max_len:
    a = '0' * (max_len - len(a)) + a

if len(b) < max_len:
    b = '0' * (max_len - len(b)) + b

if a > b:
    ans = "GREATER"
elif a == b:
    ans = "EQUAL"
else:
    ans = "LESS"

print(ans)
