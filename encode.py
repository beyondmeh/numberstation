#!/usr/bin/env python2

import sys
import random

# The number of digits in each set of numbers
digits = 5

# The number of columns of numbers in each row
cols = 10

start = int('1'.ljust(digits, '0'))
end = int('9'.ljust(digits, '9'))

# Generate the mapping that associates each ASCII decimal value with each
# grouping of digits that can represent it 
asciiMap = {}

for i in range(start, end + 1):
    mod = i % 127
    
    if mod in asciiMap:
        asciiMap[mod].insert(0, i)
    else:
        asciiMap[mod] = [i]

# Convert the message into groupings of digits
counter = 0

print "\n----- ENCODE -----"
for line in sys.stdin:
    for char in line:
        char = ord(char)
        num = random.choice(asciiMap[char])
        
        sys.stdout.write(str(num) + ' ')
        sys.stdout.flush()

        counter += 1
        
        if counter == cols:
            print ""
            counter = 0

print "\n------------------"
