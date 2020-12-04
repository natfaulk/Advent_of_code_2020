import loader
import re
import string

# PART 2 VALIDATION
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

def toInt(_val):
  try:
    out=int(_val)
    return out
  except:
    return None

# Lower and upper are inclusive
def fourDigitBetween(_val, _lower, _upper):
  if len(_val)!=4:
    return False  
  _val=toInt(_val)
  if _val is None:
    return False

  if _val<_lower or _val>_upper:
    return False

  return True

def valid_byr(_byr):
  return fourDigitBetween(_byr, 1920, 2002)

def valid_iyr(_iyr):
  return fourDigitBetween(_iyr, 2010, 2020)

def valid_eyr(_eyr):
  return fourDigitBetween(_eyr, 2020, 2030)

def valid_hgt(_hgt):
  units=_hgt[-2:]
  val=toInt(_hgt[:-2])
  if val is None:
    return False

  if units=='cm':
    return val>=150 and val<=193
  if units=='in':
    return val>=59 and val<=76

  return False

def valid_hcl(_hcl):
  if len(_hcl)!=7:
    return False
  if _hcl[0]!='#':
    return False
  return all(i in string.hexdigits for i in _hcl[1:])

POSSIBLE_ECL=['amb','blu','brn','gry','grn','hzl','oth']
def valid_ecl(_ecl):
  return _ecl in POSSIBLE_ECL

def valid_pid(_pid):
  if len(_pid)!=9:
    return False
  return _pid.isdecimal()

KEYS=[
  'ecl','pid','eyr','hcl','byr','iyr','hgt'
]

class Passport:
  def __init__(self):
    self.keys={}
    for i in KEYS:
      self.keys[i]=None

  def p1valid(self):
    for i in self.keys.values():
      if i is None:
        return False
    
    return True
  
  def p2valid(self):
    for k,v in self.keys.items():
      if v is None:
        return False

      # call validation function by building its name 
      # from "valid_" + the dictionary key
      if not globals()[f'valid_{k}'](v):
        return False
    
    return True

  def addKey(self, _key, _val):
    if _key in KEYS:
      self.keys[_key]=_val


def decodeFields(_message):
  tokens=re.split(' |\n', _message)
  p=Passport()

  for i in tokens:
    # sometimes get a 0 length input
    if len(i) == 0:
      continue

    key,val=i.split(':')
    p.addKey(key,val)
  
  return p

if __name__ == '__main__':
  data = loader.loadIn('day4.in')
  data=data.split('\n\n')

  countp1 = 0
  countp2 = 0
  for i in data:
    passport=decodeFields(i)
    if passport.p1valid():
      countp1+=1
    if passport.p2valid():
      countp2+=1

  print(countp1,countp2)

