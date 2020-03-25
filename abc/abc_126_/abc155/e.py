digits = input()
digits = list(map(int, digits[::-1]))
digits.append(0)

ans = 0
for i in range(len(digits)):
    if digits[i] < 5:
        ans += digits[i]
    elif digits[i] == 5:
        if digits[i + 1] < 5:
            ans += digits[i]
        else:
            digits[i + 1] += 1
            ans += 10 - digits[i]
    else:
        # digits[i] > 5
        digits[i + 1] += 1
        ans += 10 - digits[i]

print(ans)
