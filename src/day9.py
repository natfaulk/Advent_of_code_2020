import loader

NVAL=25

if __name__ == '__main__':
  data = loader.loadInLines('day9.in')

  numbers=[int(i) for i in data]

  outlier=None
  for i in range(NVAL, len(numbers)):
    valid=False
    for j in range(i-NVAL, i):
      if numbers[j]*2 == numbers[i]:
        continue

      if (numbers[i]-numbers[j]) in numbers[i-NVAL:i]:
        valid=True
        break
    
    if not valid:
      outlier=numbers[i]
      print(outlier)
  
  start=None
  finish=None
  for i in range(len(numbers)):
    start=i
    j=i
    sum=0
    while sum<outlier:
      sum+=numbers[j]
      j+=1
      if sum==outlier:
        finish=j
        break
    
    if finish is not None:
      break
  
  nums=numbers[start:finish]
  print(min(nums)+max(nums))





