import loader

if __name__ == '__main__':
  data = loader.loadInLines('day5.in')

  all_ids=[]
  for i in data:
    # Convert to binary F is 0, B is 1, L is 0, R is 1
    i=i.replace('F', '0')
    i=i.replace('B', '1')
    i=i.replace('L', '0')
    i=i.replace('R', '1')
    row=i[:7]
    col=i[7:]

    row=int(row,2)
    col=int(col,2)
    id=row*8+col
    all_ids.append(id)

  all_ids.sort()

  # PART 1 MAX ID
  print(all_ids[-1])

  # PART 2 MISSING ID
  prev=None
  for i in all_ids:
    if prev is not None:
      if (i-prev)!=1:
        print(prev,i, f'Seat is: {i-1}')
    prev=i
    
    
