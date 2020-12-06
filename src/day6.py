import loader

if __name__ == '__main__':
  data=loader.loadIn('day6.in')
  data=data.split('\n\n')

  count1=0
  count2=0
  for i in data:
    # PART 1
    qs = set()
    flattened=i.replace('\n','')
    for j in flattened:
      qs.add(j)
    count1+=len(qs)

    # PART 2
    i=i.split('\n')
    # loop through each letter in first string
    for j in i[0]:
      # check if in all others
      early_exit=False
      for k in i[1:]:
        #somtimes get a zero len item cause of trailing \n
        if len(k) == 0:
          continue

        if j not in k:
          early_exit=True
          break
      
      if not early_exit:
        count2+=1

  print(count1)
  print(count2)

