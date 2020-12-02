import loader

if __name__ == '__main__':
  data = loader.loadIn('day1.in')

  data_clean=[]
  for i in data:
    data_clean.append(int(i.strip()))

  # PART 1

  outs=[]
  for i in range(len(data_clean)-1):
    for j in range(i+1, len(data_clean)):
      if data_clean[i]+data_clean[j] == 2020:
        outs.append(data_clean[i]*data_clean[j])

  # PART 2

  for i in range(len(data_clean)-2):
    for j in range(i+1, len(data_clean)-1):
      for k in range(j+1, len(data_clean)):
        if data_clean[i]+data_clean[j]+data_clean[k] == 2020:
          outs.append(data_clean[i]*data_clean[j]*data_clean[k])
  
  print(outs)
