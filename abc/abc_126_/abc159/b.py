s = input()
n = len(s)


def check(t):
    for i in range(len(t)):
        if t[i] != t[len(t) - i - 1]:
            return False
    return True


ans = 'Yes' if check(s) and check(s[:(n - 1) // 2]) and check(s[(n + 1) //
                                                                2:]) else 'No'

print(ans)
