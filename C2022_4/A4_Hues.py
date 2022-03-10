from colorsys import rgb_to_hsv

colors = list(input().split())
values_teintes = []
res = 0

for color in colors:
    hsv_color = rgb_to_hsv(int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))

    if hsv_color[1] != 0:
        values_teintes.append(hsv_color[0])

values_teintes.sort()

for i in range(len(values_teintes)):
    if i == 0:
        value = abs(values_teintes[i] - values_teintes[i - 1] + 1)
        if value >= 1:
            value -= 1
    else:
        value = abs(values_teintes[i] - values_teintes[i-1])

    if value > res:
        res = value


print(f"{res:.5f}")
