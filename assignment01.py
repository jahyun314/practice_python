def hanoi_tower(n,fr,by,to):
  global count
  if (n==1):
    print("원판1: %s → %s" %(fr, to))
    count += 1
  else:
    hanoi_tower(n-1,fr,to,by)
    print("원판%d: %s → %s" %(n,fr,to))
    count +=1
    hanoi_tower(n-1,by,fr,to)



for i in range(1,5):
  count = 0
  hanoi_tower(i,"A","B","c")
  print("총횟수: %d" %(count))
  print("============================")