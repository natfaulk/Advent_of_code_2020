import loader
import copy

def decodeLine(_line):
  l=_line.split(' ')
  return [l[0],int(l[1])]

def checkProgram(_program):
  instrs_run=set()
  pc=0
  acc=0
  cleanExit=True

  while True:
    if pc >= len(_program):
      break

    if pc in instrs_run:
      cleanExit=False
      break

    instr=_program[pc]
    instrs_run.add(pc)
    if instr[0]=='jmp':
      pc+=instr[1]
      continue
      
    if instr[0]=='acc':
      acc+=instr[1]

    pc+=1

  return acc,cleanExit

if __name__ == '__main__':
  data = loader.loadInLines('day8.in')

  program=[decodeLine(i) for i in data]
  
  # PART 1
  acc,cleanExit=checkProgram(program)
  print(acc)

  # PART 2
  i=0
  while i < len(program):
    if program[i][0] != 'acc':
      program_copy=copy.deepcopy(program)
      if program_copy[i][0]=='nop':
        program_copy[i][0]='jmp'
      else:
        program_copy[i][0]='nop'
    
      acc,cleanExit=checkProgram(program_copy)
      if cleanExit:
        print(f'Clean exit, acc = {acc}')
    
    i+=1

  