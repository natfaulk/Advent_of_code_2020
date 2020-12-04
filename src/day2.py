import loader

if __name__ == '__main__':
  data_raw=loader.loadInLines('day2.in')

  count=0
  count2=0
  for i in data_raw:
    i=i.strip()
    i=i.split(' ')
    
    policy_mm=i[0].split('-')
    lower=int(policy_mm[0])
    upper=int(policy_mm[1])
    letter=i[1][0]
    pw=i[2]

    c=pw.count(letter)

    # PART1
    if c>=lower and c<=upper:
      count+=1
    
    # PART2
    t=0
    if pw[lower-1]==letter:
      t+=1
    if pw[upper-1]==letter:
      t+=1
    if t==1:
      count2+=1
  
  print(count, count2)