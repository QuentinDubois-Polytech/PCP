def main():
  V, E = map(int, input().split())
  I = [set() for _ in range(V)]
  for _ in range(E):
    a,b = map(int, input().split())
    I[b].add(a)
  S = [0]*V
  for n in range(V):
    friends = set()
    first_follower = set()
    for x in I[n]:
      if n in I[x]:
        friends.add(x)
      else:
        first_follower.add(x)
    followers = set()
    for x in friends: followers |= I[x]
    followers-=friends
    followers-=first_follower
    followers.discard(n)
    #print(friends, first_follower, followers)
    S[n]=len(followers)+2*len(first_follower)+3*len(friends)
  print(max(S))

main()