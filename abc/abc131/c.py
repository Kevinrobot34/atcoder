
def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)
def LCM(a, b):
    return a * b // GCD(a, b)

print(GCD(9, 12))
print(LCM(9, 12))
