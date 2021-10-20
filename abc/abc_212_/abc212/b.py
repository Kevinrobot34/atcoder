x = input()

if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
    ans = "Weak"
else:
    ans = "Weak"
    for i in range(3):
        if (int(x[i]) + 1) % 10 != int(x[i + 1]):
            ans = "Strong"
            break

print(ans)
