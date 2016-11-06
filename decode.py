#!/usr/bin/env python2

import sys

print "\n----- DECODE -----"

for line in sys.stdin:
  line = line.strip()
    
  for number in line.split(' '):
    number = int(number) % 127
    char = chr(number)
        
    sys.stdout.write(char)
    sys.stdout.flush()
    
print "\n------------------"
