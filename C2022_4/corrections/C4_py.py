def main():
  N, A, B, C = map(int, input().split())
  R = tuple(map(int, input().split()))
  D = {(A, B, C)}
  L = [(A, B, C)]
  dist = 0
  while R not in D:
    NL = []
    dist += 1
    for a,b,c in L:
      for p in [((a+b)%N, (b+c)%N, (c+a)%N), ((a+1)%N, (b-1)%N, c), (c, b, a)]:
        if p not in D:
          D.add(p)
          NL.append(p)
    L = NL
  print(dist)

main()