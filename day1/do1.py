import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.lib import checked, go, readInput

def calculate(data):
  digits = [str(i) for i in range(10)]
  total = 0
  for s in data:
    n1 = None
    n2 = None
    for c in s:
      if c in digits:
        if n1 == None:
          n1 = c

        n2 = c
    if n1 != None:
      total += int(n1+n2)
  
  return total
     

test = 142
if not checked(test, calculate): 
  print('CALCULATION INVALID')
else:
  print('CALCULATION VALID')
  print(f'Code:\n{go(calculate)}')