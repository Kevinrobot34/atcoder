x, y = map(int, input().split())
if y != 0:
    z = (100 * x) // y
    print(f'{z//100}.{z%100:02}')
else:
    print('ERROR')
