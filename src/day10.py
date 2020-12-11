import loader

if __name__ == '__main__':
  data = loader.loadInLines('day10.in')

  jolts=[0]+[int(i) for i in data]
  jolts+=[max(jolts)+3]
  jolts.sort()
  
  diffs=[0 for i in range(4)]
  for i in range(1,len(jolts)):
    diffs[jolts[i]-jolts[i-1]]+=1

  # PART 1
  print(diffs[1]*diffs[3])
  
  # PART 2
  # number of combinations can be worked out from the length of a sequence of ones
  # 1: 1 combination
  # 2: 2
  # 3: 4
  # 4: 7
  # 5: 13
  # 6: 24
  # 7: 44

  # The pattern is n = (n-1)+(n-2)+(n-3)

  # cache this pattern
  n_combs=[0,1,2,4,7,13]

  # extends cache if _n doesnt exist in it yet
  def get_n_combs(_n):
    while len(n_combs) <= _n:
      n_combs.append(n_combs[-1]+n_combs[-2]+n_combs[-3])
    
    return n_combs[_n]
  
  gaps=[]
  for i in range(1,len(jolts)):
    gaps.append(jolts[i]-jolts[i-1])

  combs=1
  i=0
  while i < len(gaps):
    if gaps[i]==1:
      count=1
      while gaps[i+count]==1:
        count+=1
      combs*=get_n_combs(count)
      i+=count
    else:
      i+=1
  print(combs)

  