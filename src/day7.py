import loader

def decodeLine(_line):
  s=_line.split()
  outer_bag=f'{s[0]} {s[1]}'
  
  inner_bags=[]
  if s[4]!='no':
    i=0
    while(6+i<len(s)):
      count=int(s[4+i]) 
      bag_type=f'{s[5+i]} {s[6+i]}'
      inner_bags.append((count, bag_type))
      i+=4

  return outer_bag,inner_bags

def getNumbags(_bag, _db):
  # THIS BAG
  count=1
  children=_db[_bag]
  for i in children:
    count+=i[0]*getNumbags(i[1], _db)
  return count

if __name__ == '__main__':
  data = loader.loadInLines('day7.in')

  # build db of what holds what
  db={}
  for i in data:
    outer,inner=decodeLine(i)
    db[outer]=inner
  
  # reverse the db for more efficient traversal later
  # ie db of what contains a bag type
  db_inv={}
  for k,v in db.items():
    for j in v:
      inner=j[1]
      if inner not in db_inv:
        db_inv[inner]=[]
      
      db_inv[inner].append((k, j[0]))
  
  # PART 1
  # add all parents to queue, add their parents etc until queue empty
  out=set()
  queue=db_inv['shiny gold']
  while len(queue)>0:
    t=queue.pop()
    parent=t[0]
    out.add(parent)
    if parent in db_inv:
      queue+=db_inv[parent]
  
  print(len(out))

  # PART 2
  # recursion........
  # -1 cause includes this bag
  print(getNumbags('shiny gold', db)-1)
