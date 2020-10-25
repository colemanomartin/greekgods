# Program to generate a light show for the orbit when the ball goes counter clockwise
# Invoke by typing python3 orbitcounterclockwise.py > nameOfShow.yaml

print('#show_version=5')
for i in range(2,69):
   print('- duration: 1')
   print('  lights:')
   print('    l_orbit_{0}: FFFFFF'.format(i))
   print('    l_orbit_{0}: FFFFFF'.format(i-1))
   print('    l_orbit_{0}: FFFFFF'.format(i-2))
   if (i>2):
     print('    l_orbit_{0}: 000033'.format(i-3))
