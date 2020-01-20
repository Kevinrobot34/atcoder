s = input()

if 1 <= int(s[:2]) <= 12 and 1 <= int(s[2:]) <= 12:
    print("AMBIGUOUS")
elif 1 <= int(s[2:]) <= 12:
    print("YYMM")
elif 1 <= int(s[:2]) <= 12:
    print("MMYY")
else:
    print("NA")
