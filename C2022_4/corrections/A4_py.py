from colorsys import rgb_to_hsv

def hex_to_rgb(s): return int(s[1:3],16)/255, int(s[3:5],16)/255, int(s[5:7],16)/255

C = list(map(hex_to_rgb,input().split()))
L = []
for c in C:
    h,s,_ = rgb_to_hsv(*c)
    if s>0.: L.append(h)

L.sort()

mx = max(L[i]-L[i-1] for i in range(1, len(L)))
mx = max(mx, L[0]-L[-1]+1)
print(f'{mx:.5f}')