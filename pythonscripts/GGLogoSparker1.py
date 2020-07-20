# Program to generate a light show for the logo during attract
# Invoke by typing python3 GGLogoSparker1.py > nameOfShow.yaml
# import the random module
import random

print('#show_version=5')
for i in range(0, 9):
   print('- duration: 1')
   print('  lights:')
   for j in range(7,43):
     r = random.randint(184,255)
     g = random.randint(184,255)
     b = random.randint(184,255)
     print('    l_serial_{0}: {1}{2}{3}'.format(j,hex(r)[2:],hex(g)[2:],hex(b)[2:]))
