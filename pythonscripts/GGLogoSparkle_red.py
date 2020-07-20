# Program to generate a light show for the open hades door mode
# Invoke by typing python3 GGLogoSparkle_red1.py > nameOfShow.yaml
# import the random module
import random

print('#show_version=5')
for i in range(0, 30):
   print('- duration: 1')
   print('  lights:')
   for j in range(7,43):
     a = random.randint(0,10)
     if a > 8:
         print('    l_serial_{0}: FF0000'.format(j))
     else:
         print('    l_serial_{0}: FFFFFF'.format(j))
