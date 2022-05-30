N,r = int(input()), 0
R = sorted((lambda s: (N-int(s[0]), float(s[1]), i+1))(input().split()) for i in range(N))
tw = lambda i, d: i >= 0 and i+d < N and ((R[i][0] == R[i+d][0] and R[i][1] != R[i+d][1]) or (R[i][0] < R[i+d][0] and R[i][1] >= R[i+d][1]))
for i in range(N-1):
  if tw(i,1): r = R[i+1][2] if tw(i+1,1) or tw(i-1,2) else R[i][2] if tw(i,2) else 0; break
print(r)