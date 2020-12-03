import loader
from functools import reduce

def checkSlope(_data, _right, _down):
  WIDTH=len(_data[0].strip())

  count=0
  pos=0
  for i in range(0, len(_data), _down):
    if _data[i][pos]=='#':
      count+=1
    pos+=_right
    pos%=WIDTH
  
  return count

if __name__ == '__main__':
  data=loader.loadIn('day3.in')

  # PART 1
  print(checkSlope(data,3,1))

  # PART 2
  tocheck=[
    # Right 1, down 1.
    (1,1),
    # Right 3, down 1. (This is the slope you already checked.)
    (3,1),
    # Right 5, down 1.
    (5,1),
    # Right 7, down 1.
    (7,1),
    # Right 1, down 2.
    (1,2)
  ]

  answers=[checkSlope(data,i[0],i[1]) for i in tocheck]
  out=reduce(lambda a, b: a*b, answers)
  print(out)
  