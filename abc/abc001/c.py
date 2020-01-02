deg, dis = map(int, input().split())


def round(x, d=0):
    x *= 10**d
    x = (x * 2 + 1) // 2
    x /= 10**d
    return x


power = [
    0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6, 1000
]
angle = [
    11.25, 33.75, 56.25, 78.75, 101.25, 123.75, 146.25, 168.75, 191.25, 213.75,
    236.25, 258.75, 281.25, 303.75, 326.25, 348.75, 371.25
]
angle_symbol = [
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW',
    'W', 'WNW', 'NW', 'NNW', 'N'
]
len(angle)

# print(dis, dis / 60.0, round(dis / 60.0, 1))
dis = round(dis / 60.0, d=1)
ans_dis = 0
for i in range(len(power)):
    if dis <= power[i]:
        # print(i, dis, power[i])
        ans_dis = i
        break

deg = deg / 10.0
ans_deg = 0
for i in range(len(angle)):
    if deg < angle[i]:
        # print(i, deg, angle[i])
        ans_deg = angle_symbol[i]
        break

if ans_dis == 0:
    ans_deg = 'C'

print(ans_deg, ans_dis)
