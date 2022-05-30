from collections import defaultdict

MOD = 2**59-55
OFF = ord('A')


def compare(s, n, l):
  t = [True]*len(l)
  for i in range(len(l)):
    if t[i]:
      t[i] = False
      res, wit = 1, s[l[i]:l[i]+n]
      for j in range(i+1, len(l)):
        if wit == s[l[j]:l[j]+n]:
          res += 1
          t[j] = False
          if res == 3:
            return True
  return False


def find_3(s, n):
  D = defaultdict(list)
  if n > len(s)-2:
    return False
  if n == 0:
    return True
  key = 0
  rem = pow(26, n-1, MOD)
  for i in range(n):
    key = (key*26+ord(s[i])-OFF) % MOD
  D[key].append(0)
  for i in range(n, len(s)):
    key = (key-rem*(ord(s[i-n])-OFF))
    key = (key*26+ord(s[i])-OFF) % MOD
    D[key].append(i-n+1)
    if len(D[key]) > 2:
      if compare(s, n, D[key]):
        return True
  return False


def main(s):
  a, b = 0, len(s)-2
  while b-a > 1:
    m = (b+a)//2
    if find_3(s, m):
      a = m
    else:
      b = m
  print(a)


main(input())
